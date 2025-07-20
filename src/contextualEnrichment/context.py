#!/usr/bin/env python3
"""
Document Contextualization CLI Application

This module provides intelligent chunking and contextualization of markdown documents
using local LLM processing via Ollama or remote models via OpenRouter. It splits documents 
into semantic chunks and adds contextual information to improve search and retrieval.

Features:
- Semantic document chunking using LLM guidance
- Contextual enrichment of chunks
- Batch processing of markdown files
- Configurable LLM models (local via Ollama or remote via OpenRouter)
"""

import argparse
import json
import os
import re
import sys
import textwrap
from pathlib import Path
from typing import List, Optional

import requests
from ollama import chat


def validate_markdown_file(file_path: str) -> Path:
    """
    Validate that the provided file path exists and is a valid markdown file.
    
    Args:
        file_path: Path to the markdown file
        
    Returns:
        Path object for the validated file
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file is not a markdown file
    """
    if not file_path:
        raise ValueError("File path cannot be empty")
    
    md_path = Path(file_path)
    
    if not md_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not md_path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    
    if md_path.suffix.lower() != '.md':
        raise ValueError(f"File must be a markdown file: {file_path}")
    
    return md_path


def check_ollama_connection() -> bool:
    """
    Check if Ollama is running and accessible.
    
    Returns:
        True if Ollama is accessible, False otherwise
    """
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        return response.status_code == 200
    except Exception:
        return False


def clean_thinking_tags(text: str) -> str:
    """
    Remove <think> and </think> tags and their content from the response.
    
    Args:
        text: Text that may contain thinking tags
        
    Returns:
        Cleaned text without thinking tags and content
    """
    # Remove <think>...</think> blocks (including multiline)
    cleaned = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    
    # Clean up any extra whitespace left behind
    cleaned = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned)
    
    return cleaned.strip()


def call_model_remote(prompt: str, model: str, temperature: float = 0.0) -> str:
    """
    Call a remote model via OpenRouter API.
    
    Args:
        prompt: The prompt to send to the model
        model: Model name (e.g., "openai/gpt-4o-mini")
        temperature: Sampling temperature
        
    Returns:
        Model response text
        
    Raises:
        Exception: If model call fails
    """
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise Exception("OPENROUTER_API_KEY environment variable not found")
    
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            data=json.dumps({
                "model": model,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "temperature": temperature,
                "max_tokens": 16384
            })
        )
        response.raise_for_status()
        result = response.json()
        
        content = result['choices'][0]['message']['content']
        return clean_thinking_tags(content)
        
    except Exception as e:
        raise Exception(f"Failed to call remote model {model}: {str(e)}")


def call_model_local(prompt: str, model: str, temperature: float = 0.0) -> str:
    """
    Call a local model via Ollama.
    
    Args:
        prompt: The prompt to send to the model
        model: Model name
        temperature: Sampling temperature
        
    Returns:
        Model response text
        
    Raises:
        Exception: If model call fails
    """
    try:
        response = chat(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            # keep_alive="-1h",
            options={
                "num_ctx": 16384,
                "temperature": temperature,
                "min_p": 0.01,
                "repeat_penalty": 1.0,
                "top_k": 64,
                "top_p": 0.95,
            },
        )
        content = response.message.content
        return clean_thinking_tags(content)
        
    except Exception as e:
        raise Exception(f"Failed to call local model {model}: {str(e)}")


def call_model(prompt: str, model: str = "deepseek-r1:8b", temperature: float = 0.0, use_remote: bool = False) -> str:
    """
    Call either a local or remote LLM model.
    
    Args:
        prompt: The prompt to send to the model
        model: Model name to use
        temperature: Sampling temperature (default: 0.0 for deterministic)
        use_remote: Whether to use remote API via OpenRouter
        
    Returns:
        Model response text
        
    Raises:
        Exception: If model call fails
    """
    if use_remote:
        return call_model_remote(prompt, model, temperature)
    else:
        return call_model_local(prompt, model, temperature)


def save_prompt(prompt: str, source_filename: str, prompt_type: str, chunk_index: Optional[int] = None) -> Path:
    """
    Save a prompt as a markdown file in the prompts folder.
    
    Args:
        prompt: The prompt text to save
        source_filename: Name of the source file (without extension)
        prompt_type: Type of prompt ("chunking" or "contextualization")
        chunk_index: Index of chunk for contextualization prompts
        
    Returns:
        Path to the saved prompt file
    """
    # Create prompts directory
    prompts_dir = Path("src/contextualEnrichment/prompts")
    prompts_dir.mkdir(parents=True, exist_ok=True)
    
    # Create filename
    if chunk_index is not None:
        prompt_filename = f"{source_filename}_PROMPT_{prompt_type}_chunk_{chunk_index:02d}.md"
    else:
        prompt_filename = f"{source_filename}_PROMPT_{prompt_type}.md"
    
    prompt_path = prompts_dir / prompt_filename
    
    # Create markdown content with metadata
    timestamp = Path().resolve().name  # Simple timestamp alternative
    content = f"""# {prompt_type.title()} Prompt

**Source File:** {source_filename}  
**Prompt Type:** {prompt_type.title()}  
**Generated:** {timestamp}  
{"**Chunk Index:** " + str(chunk_index) + "  " if chunk_index is not None else ""}

---

{prompt}
"""
    
    # Save to file
    with open(prompt_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return prompt_path


def create_initial_chunks(document_text: str, split_pattern: str = "\n#") -> str:
    """
    Create initial chunks from document text with markers.
    
    Args:
        document_text: The full document text
        split_pattern: Pattern to split on (default: "\n#")
        
    Returns:
        Text with chunk markers added
    """
    chunks = document_text.split(split_pattern)
    
    chunked_text = ""
    for i, chunk in enumerate(chunks):
        if chunk.startswith("#"):
            chunk = f"#{chunk}"  # add the # back to the chunk
        chunked_text += f"<|start_chunk_{i}|>\n{chunk}<|end_chunk_{i}|>"
    
    return chunked_text


def get_semantic_split_points(chunked_text: str, model: str, source_filename: str, use_remote: bool = False) -> List[int]:
    """
    Use LLM to determine semantic split points for chunks.
    
    Args:
        chunked_text: Text with chunk markers
        model: LLM model to use
        source_filename: Name of source file for prompt saving
        use_remote: Whether to use remote API
        
    Returns:
        List of chunk indices where splits should occur
    """
    chunking_prompt = """
You are an assistant specialized in splitting text into semantically consistent sections.

<instructions>
    <instruction>The text has been divided into chunks, each marked with <|start_chunk_X|> and <|end_chunk_X|> tags, where X is the chunk number</instruction>
    <instruction>Identify points where splits should occur, such that consecutive chunks of similar themes stay together</instruction>
    <instruction>Each chunk must be between 200 and 1000 words</instruction>
    <instruction>If chunks 1 and 2 belong together but chunk 3 starts a new topic, suggest a split after chunk 2</instruction>
    <instruction>The chunks must be listed in ascending order</instruction>
    <instruction>Provide your response in the form: 'split_after: 3, 5'</instruction>
</instructions>

This is the document text:
<document>
{document_text}
</document>

Respond only with the IDs of the chunks where you believe a split should occur. 
YOU MUST RESPOND WITH AT LEAST ONE SPLIT.
""".strip()

    prompt = chunking_prompt.format(document_text=chunked_text)
    
    # Save the prompt
    try:
        save_prompt(prompt, source_filename, "chunking")
        print(f"  ✓ Saved chunking prompt")
    except Exception as e:
        print(f"  ⚠️  Warning: Failed to save chunking prompt: {e}")
    
    response = call_model(prompt, model, use_remote=use_remote)
    
    # Extract split points from LLM response
    split_after = []
    if "split_after:" in response:
        split_points = response.split("split_after:")[1].strip()
        try:
            split_after = [int(x.strip()) for x in split_points.split(",") if x.strip()]
        except ValueError:
            print("⚠️  Warning: Could not parse split points from LLM response")
            # Fallback: split every 3 chunks
            split_after = [2, 5, 8]
    
    return split_after


def split_text_by_llm_suggestions(chunked_text: str, split_after: List[int]) -> List[str]:
    """
    Split text according to LLM suggestions.
    
    Args:
        chunked_text: Text with chunk markers
        split_after: List of chunk indices to split after
        
    Returns:
        List of text sections
    """
    # If no splits were suggested, return the whole text as one section
    if not split_after:
        return [chunked_text]

    # Find all chunk markers in the text
    chunk_pattern = r"<\|start_chunk_(\d+)\|>(.*?)<\|end_chunk_\1\|>"
    chunks = re.findall(chunk_pattern, chunked_text, re.DOTALL)

    # Group chunks according to split points
    sections = []
    current_section = []

    for chunk_id, chunk_text in chunks:
        current_section.append(chunk_text)
        if int(chunk_id) in split_after:
            sections.append("".join(current_section).strip())
            current_section = []

    # Add the last section if it's not empty
    if current_section:
        sections.append("".join(current_section).strip())

    return sections


def contextualize_chunk(chunk: str, document_text: str, model: str, source_filename: str, chunk_index: int, use_remote: bool = False, save_prompt_once: bool = False) -> str:
    """
    Generate contextual information for a chunk.
    
    Args:
        chunk: The chunk text to contextualize
        document_text: The full document text
        model: LLM model to use
        source_filename: Name of source file for prompt saving
        chunk_index: Index of the current chunk
        use_remote: Whether to use remote API
        save_prompt_once: Whether to save the prompt (only for first chunk)
        
    Returns:
        Contextual description of the chunk
    """
    contextualizer_prompt = """
You are an assistant specialized in analyzing document chunks and providing relevant context.

<instructions>
    <instruction>You will be given a document and a specific chunk from that document</instruction>
    <instruction>Provide 2-3 concise sentences that situate this chunk within the broader document</instruction>
    <instruction>Identify the main topic or concept discussed in the chunk</instruction>
    <instruction>Include relevant information or comparisons from the broader document context</instruction>
    <instruction>Note how this information relates to the overall theme or purpose of the document if applicable</instruction>
    <instruction>Include key figures, dates, or percentages that provide important context</instruction>
    <instruction>Avoid phrases like "This chunk discusses" - instead, directly state the context</instruction>
    <instruction>Keep your response brief and focused on improving search retrieval</instruction>
</instructions>

Here is the document:
<document>
{document}
</document>

Here is the chunk to contextualize:
<chunk>
{chunk}
</chunk>

Respond only with the succinct context for this chunk. Do not mention it is a chunk or that you are providing context.
""".strip()

    prompt = contextualizer_prompt.format(document=document_text, chunk=chunk)
    
    # Save the prompt only once (for the first chunk) since they're all the same structure
    if save_prompt_once:
        try:
            save_prompt(prompt, source_filename, "contextualization")
            print(f"    ✓ Saved contextualization prompt template")
        except Exception as e:
            print(f"    ⚠️  Warning: Failed to save contextualization prompt: {e}")
    
    return call_model(prompt, model, use_remote=use_remote)


def process_markdown_file(file_path: Path, model: str = "deepseek-r1:8b", use_remote: bool = False) -> str:
    """
    Process a markdown file with chunking and contextualization.
    
    Args:
        file_path: Path to the markdown file
        model: LLM model to use
        use_remote: Whether to use remote API via OpenRouter
        
    Returns:
        Processed content with contextualized chunks
        
    Raises:
        Exception: If processing fails
    """
    try:
        print(f"📄 Reading: {file_path.name}")
        source_filename = file_path.stem
        
        # Read the document
        with open(file_path, 'r', encoding='utf-8') as f:
            document_text = f.read()
        
        if not document_text.strip():
            raise Exception("Document is empty")
        
        print("🔄 Creating initial chunks...")
        chunked_text = create_initial_chunks(document_text)
        
        print("🤖 Getting semantic split suggestions from LLM...")
        split_points = get_semantic_split_points(chunked_text, model, source_filename, use_remote)
        print(f"✓ Found {len(split_points)} split points: {split_points}")
        
        print("✂️  Splitting text according to LLM suggestions...")
        llm_chunks = split_text_by_llm_suggestions(chunked_text, split_points)
        print(f"✓ Created {len(llm_chunks)} semantic sections")
        
        print("💭 Contextualizing chunks...")
        contextualized_chunks = []
        for i, chunk in enumerate(llm_chunks):
            print(f"  Processing chunk {i+1}/{len(llm_chunks)}...")
            # Only save prompt for the first chunk since they're all the same structure
            save_prompt_once = (i == 0)
            context = contextualize_chunk(chunk, document_text, model, source_filename, i+1, use_remote, save_prompt_once)
            
            # Format the chunk with context
            formatted_chunk = f"<chunk_context>{context}</chunk_context>\n<chunk>{chunk}</chunk>"
            contextualized_chunks.append(formatted_chunk)
        
        # Combine all chunks
        final_content = "\n\n---\n\n".join(contextualized_chunks)
        
        print("✅ Contextualization completed")
        return final_content
        
    except Exception as e:
        raise Exception(f"Failed to process {file_path.name}: {str(e)}")


def save_contextualized_result(content: str, source_path: Path, output_dir: Path, use_remote: bool = False) -> Path:
    """
    Save the contextualized content to a file.
    
    Args:
        content: The contextualized content
        source_path: Original file path
        output_dir: Output directory
        use_remote: Whether remote API was used
        
    Returns:
        Path to the saved file
        
    Raises:
        OSError: If file creation fails
    """
    try:
        # Create markdown subdirectory
        markdown_dir = output_dir / "markdown"
        markdown_dir.mkdir(parents=True, exist_ok=True)
        
        # Create output filename with _CHUNKED suffix
        output_file = markdown_dir / f"{source_path.stem}_CHUNKED.md"
        
        # Create enhanced markdown content with header
        processing_method = "Remote LLM via OpenRouter" if use_remote else "Local LLM via Ollama"
        header = f"""# Contextualized Document: {source_path.stem}

**Source:** {source_path.name}  
**Processing:** Semantic Chunking + Contextualization  
**Processed by:** {processing_method}  
**Prompts saved to:** src/contextualEnrichment/prompts/

This document has been processed to create semantic chunks with contextual information for improved search and retrieval.

---

"""
        
        full_content = header + content
        
        # Write content to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(full_content)
            
        print(f"✓ Saved to: {output_file}")
        return output_file
        
    except Exception as e:
        raise OSError(f"Failed to save contextualized file: {e}")


def find_markdown_files(directory: Path) -> List[Path]:
    """
    Find all markdown files in a directory.
    
    Args:
        directory: Directory to search
        
    Returns:
        List of markdown file paths
    """
    markdown_files = []
    if directory.exists() and directory.is_dir():
        for file_path in directory.glob("*.md"):
            # Skip already processed files
            if not file_path.name.endswith("_CHUNKED.md"):
                markdown_files.append(file_path)
    return markdown_files


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Process markdown files with semantic chunking and contextualization",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process single file (remote by default)
  python context.py file.md
  
  # Process with local Ollama model
  python context.py file.md --local
  
  # Process all markdown files in assets/markdown
  python context.py --batch
  
  # Batch process with local model
  python context.py --batch --local
  
  # Use specific remote model
  python context.py file.md --model anthropic/claude-3-haiku
  
  # Use specific local model
  python context.py file.md --local --model llama3.2:3b
  
  # Custom output directory
  python context.py file.md --output-dir custom_output

Remote Requirements (default):
  - OPENROUTER_API_KEY environment variable set
  - Valid OpenRouter API key with credits

Local Requirements:
  - Ollama running locally
  - A suitable LLM model installed (e.g., qwen2.5:3b, llama3.2:3b)
        """
    )
    
    parser.add_argument(
        'markdown_file',
        nargs='?',
        help='Path to the markdown file to process'
    )
    
    parser.add_argument(
        '--batch',
        action='store_true',
        help='Process all markdown files in assets/markdown directory'
    )
    
    parser.add_argument(
        '--model',
        default='openai/gpt-4o-mini',
        help='Model to use (default: openai/gpt-4o-mini for remote, qwen2.5:3b for local)'
    )
    
    parser.add_argument(
        '--local',
        action='store_true',
        help='Use local Ollama model instead of OpenRouter API'
    )
    
    parser.add_argument(
        '--output-dir',
        default='assets',
        help='Output directory (default: assets)'
    )
    
    args = parser.parse_args()
    
    # Validate arguments
    if not args.batch and not args.markdown_file:
        parser.error("Must specify either a markdown file or use --batch flag")
    
    # Determine processing mode and model
    use_remote = not args.local
    if args.local and args.model == 'openai/gpt-4o-mini':
        # User specified --local but didn't change model, use local default
        model = 'qwen2.5:3b'
    else:
        model = args.model
    
    try:
        # Check requirements based on usage mode
        if use_remote:
            api_key = os.environ.get("OPENROUTER_API_KEY")
            if not api_key:
                raise Exception("OPENROUTER_API_KEY environment variable not found for remote usage")
            print(f"🌐 Using remote model: {model}")
        else:
            if not check_ollama_connection():
                raise Exception("Ollama is not running. Please start Ollama service first.")
            print(f"🏠 Using local model: {model}")
        
        output_dir = Path(args.output_dir)
        files_to_process = []
        
        if args.batch:
            # Process all markdown files in assets/markdown
            markdown_dir = Path("assets/markdown")
            if not markdown_dir.exists():
                raise Exception(f"Directory not found: {markdown_dir}")
            
            files_to_process = find_markdown_files(markdown_dir)
            if not files_to_process:
                raise Exception(f"No markdown files found in {markdown_dir}")
            
            print(f"🔍 Found {len(files_to_process)} markdown files to process")
        else:
            # Process single file
            file_path = validate_markdown_file(args.markdown_file)
            files_to_process = [file_path]
        
        # Process files
        successful = 0
        failed = 0
        
        for file_path in files_to_process:
            try:
                print(f"\n🚀 Processing: {file_path}")
                content = process_markdown_file(file_path, model, use_remote)
                save_contextualized_result(content, file_path, output_dir, use_remote)
                successful += 1
                
            except Exception as e:
                print(f"❌ Failed to process {file_path}: {str(e)}")
                failed += 1
                continue
        
        # Summary
        print(f"\n📊 Processing Summary:")
        print(f"✅ Successful: {successful}")
        if failed > 0:
            print(f"❌ Failed: {failed}")
        
        if successful > 0:
            print(f"📁 Output directory: {output_dir / 'markdown'}")
        
    except KeyboardInterrupt:
        print(f"\n⏹️  Processing interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()