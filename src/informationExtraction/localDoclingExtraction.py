#!/usr/bin/env python3
"""
Local PDF Processing CLI Application using Docling

This module provides a command-line interface for processing PDF files using
local tools: Docling for PDF conversion, Ollama for VLM processing, and 
HuggingFace models for enhanced OCR capabilities.

Features:
- Local PDF to markdown conversion with image extraction
- Advanced OCR using HuggingFace models via Ollama
- Image processing and description generation
- No external API dependencies
"""

import argparse
import base64
import sys
from io import BytesIO
from pathlib import Path
from typing import Optional

import numpy as np
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    RapidOcrOptions,
    VlmPipelineOptions,
    smolvlm_picture_description,
)
from docling.datamodel.pipeline_options_vlm_model import ApiVlmOptions, ResponseFormat
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.pipeline.vlm_pipeline import VlmPipeline
from PIL import Image


def validate_pdf_file(file_path: str) -> Path:
    """
    Validate that the provided file path exists and is a valid PDF file.
    
    Args:
        file_path: Path to the PDF file
        
    Returns:
        Path object for the validated file
        
    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file is not a PDF
    """
    if not file_path:
        raise ValueError("File path cannot be empty")
    
    pdf_path = Path(file_path)
    
    if not pdf_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    if not pdf_path.is_file():
        raise ValueError(f"Path is not a file: {file_path}")
    
    if pdf_path.suffix.lower() != '.pdf':
        raise ValueError(f"File must be a PDF: {file_path}")
    
    return pdf_path


def check_ollama_connection() -> bool:
    """
    Check if Ollama is running and accessible.
    
    Returns:
        True if Ollama is accessible, False otherwise
    """
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        return response.status_code == 200
    except Exception:
        return False


def create_vlm_options(model: str, prompt: str, timeout: int = 300) -> ApiVlmOptions:
    """
    Create VLM (Vision Language Model) options for enhanced OCR processing.
    
    Args:
        model: HuggingFace model identifier
        prompt: Prompt for the VLM processing
        timeout: Request timeout in seconds (default: 180)
        
    Returns:
        Configured ApiVlmOptions
    """
    return ApiVlmOptions(
        url="http://localhost:11434/v1/chat/completions",
        params=dict(model=model),
        prompt=prompt,
        timeout=timeout,
        scale=1.0,
        response_format=ResponseFormat.MARKDOWN,
    )


def check_ollama_model(model: str) -> bool:
    """
    Check if the specified model is available in Ollama.
    
    Args:
        model: Model identifier to check
        
    Returns:
        True if model is available, False otherwise
    """
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=10)
        if response.status_code == 200:
            models = response.json().get('models', [])
            model_names = [m.get('name', '') for m in models]
            # Check if model exists (handle different naming formats)
            for model_name in model_names:
                if model in model_name or model.split('/')[-1] in model_name:
                    return True
        return False
    except Exception:
        return False


def get_available_models() -> list:
    """
    Get list of available models from Ollama.
    
    Returns:
        List of available model names
    """
    try:
        import requests
        response = requests.get("http://localhost:11434/api/tags", timeout=10)
        if response.status_code == 200:
            models = response.json().get('models', [])
            return [m.get('name', '') for m in models]
        return []
    except Exception:
        return []


def image_to_base64(image: Image.Image) -> str:
    """
    Convert PIL Image to base64 string.
    
    Args:
        image: PIL Image object
        
    Returns:
        Base64 encoded string of the image
    """
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


def process_pdf_basic(pdf_path: Path) -> str:
    """
    Process PDF using basic docling pipeline with image extraction.
    
    Args:
        pdf_path: Path to the PDF file
        
    Returns:
        Markdown content with image descriptions
        
    Raises:
        Exception: If PDF processing fails
    """
    try:
        print("🔄 Setting up basic PDF processing pipeline...")
        
        # Configure pipeline for basic processing with image extraction
        pipeline_options = PdfPipelineOptions(
            generate_page_images=True,
            images_scale=1.00,
            do_ocr=True,
            do_picture_description=True,
            ocr_options=RapidOcrOptions(),
            picture_description_options=smolvlm_picture_description,
        )
        
        converter = DocumentConverter(
            format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)}
        )
        
        print(f"📄 Processing: {pdf_path.name}")
        result = converter.convert(pdf_path)
        document = result.document
        
        print(f"✓ Found {len(document.pictures)} images in document")
        
        # Extract annotations for images
        annotations = []
        for picture in document.pictures:
            for annotation in picture.annotations:
                annotations.append(annotation.text)
        
        # Export to markdown with placeholders
        IMAGE_PLACEHOLDER = "<!-- image_placeholder -->"
        PAGE_BREAK_PLACEHOLDER = "<!-- page_break -->"
        
        text = document.export_to_markdown(
            page_break_placeholder=PAGE_BREAK_PLACEHOLDER, 
            image_placeholder=IMAGE_PLACEHOLDER
        )
        
        # Replace image placeholders with descriptions if available
        if annotations:
            print(f"✓ Adding {len(annotations)} image descriptions")
            text = replace_image_placeholders(text, IMAGE_PLACEHOLDER, annotations)
        
        return text
        
    except Exception as e:
        raise Exception(f"Failed to process PDF with basic pipeline: {str(e)}")


def process_pdf_enhanced(pdf_path: Path, page_range: Optional[list] = None, timeout: int = 300) -> str:
    """
    Process PDF using enhanced VLM pipeline via Ollama.
    
    Args:
        pdf_path: Path to the PDF file
        page_range: Optional page range to process [start, end]
        timeout: Request timeout in seconds (default: 300)
        
    Returns:
        Enhanced markdown content from VLM processing
        
    Raises:
        Exception: If enhanced processing fails
    """
    try:
        print("🚀 Setting up enhanced VLM processing pipeline...")
        
        if not check_ollama_connection():
            raise Exception("Ollama is not running. Please start Ollama service first.")
        
        # Use the required vision model
        required_model = "hf.co/unsloth/Nanonets-OCR-s-GGUF:Q4_K_M"
        
        print("🔍 Checking for required vision model...")
        
        if not check_ollama_model(required_model):
            available_models = get_available_models()
            print(f"📋 Available models: {', '.join(available_models) if available_models else 'None'}")
            raise Exception(f"Required model '{required_model}' not found in Ollama.\n"
                          f"Please install it with: ollama pull {required_model}")
        
        selected_model = required_model
        print(f"✓ Using required model: {selected_model}")
        
        # Configure VLM pipeline with selected model and timeout
        pipeline_options = VlmPipelineOptions(
            enable_remote_services=True,
            vlm_options=create_vlm_options(
                model=selected_model,
                prompt="OCR the full page to markdown with detailed descriptions of any images, tables, and formatting. Be thorough but concise.",
                timeout=timeout
            ),
        )
        
        doc_converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(
                    pipeline_options=pipeline_options,
                    pipeline_cls=VlmPipeline,
                )
            }
        )
        
        print(f"📄 Processing: {pdf_path.name}")
        print(f"⏱️  Timeout set to: {timeout} seconds")
        
        if page_range:
            print(f"📑 Processing pages {page_range[0]}-{page_range[1]}")
            result = doc_converter.convert(pdf_path, page_range=page_range)
        else:
            print("📄 Processing all pages...")
            result = doc_converter.convert(pdf_path)
        
        document = result.document
        markdown_content = document.export_to_markdown()
        
        print("✓ Enhanced VLM processing completed")
        return markdown_content
        
    except Exception as e:
        error_msg = str(e)
        if "ReadTimeout" in error_msg:
            raise Exception(f"Processing timed out after {timeout} seconds. Try:\n"
                          f"  1. Use --timeout to increase timeout\n"
                          f"  2. Process fewer pages with --pages\n"
                          f"  3. Use basic mode instead (remove --enhanced)\n"
                          f"  4. Try a faster model")
        else:
            raise Exception(f"Failed to process PDF with enhanced pipeline: {error_msg}")


def replace_image_placeholders(text: str, placeholder: str, replacements: list) -> str:
    """
    Replace image placeholders with actual descriptions.
    
    Args:
        text: Text containing placeholders
        placeholder: Placeholder string to replace
        replacements: List of replacement strings
        
    Returns:
        Text with placeholders replaced
        
    Raises:
        ValueError: If not enough placeholders for replacements
    """
    for i, replacement in enumerate(replacements):
        if placeholder in text:
            # Create a more descriptive image reference
            image_markdown = f"![Image {i+1}: {replacement}](image_{i+1}.png)\n\n_{replacement}_"
            text = text.replace(placeholder, image_markdown, 1)
        else:
            print(f"⚠️  Warning: No more placeholders found for replacement {i+1}")
            break
    return text


def save_markdown_result(content: str, source_name: str, output_dir: Path, method: str) -> Path:
    """
    Save the extracted markdown content to a file in the markdown directory.
    
    Args:
        content: The markdown content to save
        source_name: Base name for the output file (without extension)
        output_dir: Base output directory (will create 'markdown' subdirectory)
        method: Processing method used ("basic" or "enhanced")
        
    Returns:
        Path to the saved markdown file
        
    Raises:
        OSError: If file creation fails
    """
    try:
        # Create markdown subdirectory
        markdown_dir = output_dir / "markdown"
        markdown_dir.mkdir(parents=True, exist_ok=True)
        
        # Create output filename with method suffix
        output_file = markdown_dir / f"{source_name}_DOCLING_{method}.md"
        
        # Create enhanced markdown content with header
        markdown_content = f"""# Local PDF Processing Result: {source_name}

**Source:** {source_name}.pdf  
**Processing Method:** {method.title()}  
**Processed by:** Docling + {"Ollama VLM" if method == "enhanced" else "Basic OCR"}

---

{content}
"""
        
        # Write content to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
            
        print(f"✓ Markdown saved to: {output_file}")
        return output_file
        
    except Exception as e:
        raise OSError(f"Failed to save markdown file: {e}")


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Process PDF files using local tools (Docling + Ollama)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic processing (faster, local OCR only)
  python localDoclingExtraction.py document.pdf
  
  # Enhanced processing with VLM (requires Ollama)
  python localDoclingExtraction.py document.pdf --enhanced
  
  # Enhanced with longer timeout (for large/complex PDFs)
  python localDoclingExtraction.py document.pdf --enhanced --timeout 600
  
  # Process specific page range with enhanced method
  python localDoclingExtraction.py document.pdf --enhanced --pages 1 5
  
  # Custom output directory
  python localDoclingExtraction.py document.pdf --output-dir custom_output

Requirements:
  - Docling library installed
  - For enhanced processing: Ollama running with required vision model
  
Required Ollama model (install with 'ollama pull <model>'):
  - hf.co/unsloth/Nanonets-OCR-s-GGUF:Q4_K_M
        """
    )
    
    parser.add_argument(
        'pdf_file', 
        help='Path to the PDF file to process'
    )
    
    parser.add_argument(
        '--enhanced',
        action='store_true',
        help='Use enhanced VLM processing via Ollama (slower but more accurate)'
    )
    
    parser.add_argument(
        '--pages',
        nargs=2,
        type=int,
        metavar=('START', 'END'),
        help='Page range to process (only for enhanced mode), e.g., --pages 1 5'
    )
    
    parser.add_argument(
        '--timeout',
        type=int,
        default=300,
        help='Timeout for enhanced processing in seconds (default: 300)'
    )
    
    parser.add_argument(
        '--output-dir',
        default='assets',
        help='Output directory for markdown files (default: assets)'
    )
    
    args = parser.parse_args()
    
    try:
        # Validate input
        pdf_path = validate_pdf_file(args.pdf_file)
        output_dir = Path(args.output_dir)
        
        print(f"🔍 Starting local PDF processing for: {pdf_path}")
        
        if args.enhanced:
            # Enhanced processing with VLM
            print("🚀 Using enhanced VLM processing...")
            page_range = args.pages if args.pages else None
            content = process_pdf_enhanced(pdf_path, page_range, args.timeout)
            method = "enhanced"
        else:
            # Basic processing
            print("⚡ Using basic processing...")
            if args.pages:
                print("⚠️  Warning: Page range only supported in enhanced mode")
            if args.timeout != 300:
                print("⚠️  Warning: Timeout only applies to enhanced mode")
            content = process_pdf_basic(pdf_path)
            method = "basic"
        
        # Save result
        output_path = save_markdown_result(content, pdf_path.stem, output_dir, method)
        
        print(f"\n✅ Successfully processed {pdf_path}")
        print(f"📄 Output saved to: {output_path}")
        print(f"🔧 Method used: {method.title()}")
        
    except KeyboardInterrupt:
        print(f"\n⏹️  Processing interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()