#!/usr/bin/env python3
"""
RODEOS Semantic Model Extraction CLI Application

This module analyzes chunked markdown documents and creates semantic models
based on the RODEOS JSON structure. It uses OpenRouter API for LLM analysis
to determine asset types and populate metadata fields.

Features:
- Analysis of chunked markdown files with context
- Multi-step LLM analysis via OpenRouter
- Automatic asset type detection (Dataset/Model/Service)
- JSON structure validation
- Submodel selection and integration
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

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


def get_openrouter_api_key() -> str:
    """
    Get the OpenRouter API key from environment variables.
    
    Returns:
        The API key string
        
    Raises:
        ValueError: If API key is not found
    """
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError(
            "OPENROUTER_API_KEY environment variable not found. "
            "Please set it with your OpenRouter API key."
        )
    return api_key


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
    cleaned = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
    cleaned = re.sub(r'\n\s*\n\s*\n', '\n\n', cleaned)
    return cleaned.strip()


def call_model_local(prompt: str, model: str, temperature: float = 0.1) -> str:
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
            keep_alive="-1h",
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


def call_model_local_with_json_validation(prompt: str, model: str, temperature: float = 0.1, max_retries: int = 3) -> Dict:
    """
    Call local Ollama model with JSON validation and retry logic.
    
    Args:
        prompt: The prompt to send to the model
        model: Model name to use
        temperature: Sampling temperature (low for consistency)
        max_retries: Maximum number of retry attempts
        
    Returns:
        Parsed JSON dictionary
        
    Raises:
        Exception: If model call fails or JSON cannot be parsed after retries
    """
    for attempt in range(max_retries):
        try:
            raw_response = call_model_local(prompt, model, temperature)
            
            try:
                json_str = extract_json_from_response(raw_response)
                return json.loads(json_str)
            except (json.JSONDecodeError, ValueError) as json_error:
                if attempt < max_retries - 1:
                    feedback_prompt = f"""
{prompt}

IMPORTANT: Your previous response was not valid JSON. Please respond with ONLY a valid JSON object, no explanations or additional text.

Previous invalid response: {raw_response[:200]}...

Error: {str(json_error)}

Respond with ONLY valid JSON:
"""
                    prompt = feedback_prompt
                    print(f"⚠️  Retry {attempt + 1}/{max_retries}: JSON parsing failed, retrying with feedback...")
                    continue
                else:
                    raise Exception(f"Failed to get valid JSON after {max_retries} attempts: {json_error}")
        except Exception as e:
            if attempt == max_retries - 1:
                raise Exception(f"Failed to call local model: {str(e)}")
            continue
    
    raise Exception("Unexpected error in local model call")


def extract_json_from_response(response: str) -> str:
    """
    Extract JSON from a response that might contain additional text.
    
    Args:
        response: The raw response from the API
        
    Returns:
        Extracted JSON string
        
    Raises:
        ValueError: If no valid JSON found
    """
    # Try to find JSON in the response
    response = response.strip()
    
    # Look for JSON block markers
    if "```json" in response:
        start = response.find("```json") + 7
        end = response.find("```", start)
        if end != -1:
            return response[start:end].strip()
    
    # Look for JSON object boundaries
    start_brace = response.find('{')
    if start_brace != -1:
        # Find the matching closing brace
        brace_count = 0
        for i, char in enumerate(response[start_brace:], start_brace):
            if char == '{':
                brace_count += 1
            elif char == '}':
                brace_count -= 1
                if brace_count == 0:
                    return response[start_brace:i+1]
    
    # If no braces found, try the whole response
    return response


def call_openrouter_api_with_json_validation(prompt: str, model: str = "openai/gpt-4o-mini", temperature: float = 0.1, max_retries: int = 3) -> Dict:
    """
    Call OpenRouter API with JSON validation and retry logic.
    
    Args:
        prompt: The prompt to send to the model
        model: Model name to use
        temperature: Sampling temperature (low for consistency)
        max_retries: Maximum number of retry attempts
        
    Returns:
        Parsed JSON dictionary
        
    Raises:
        Exception: If API call fails or JSON cannot be parsed after retries
    """
    api_key = get_openrouter_api_key()
    
    for attempt in range(max_retries):
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
            
            raw_response = result['choices'][0]['message']['content']
            
            # Try to extract and parse JSON
            try:
                json_str = extract_json_from_response(raw_response)
                return json.loads(json_str)
            except (json.JSONDecodeError, ValueError) as json_error:
                if attempt < max_retries - 1:
                    # Add feedback to the prompt for retry
                    feedback_prompt = f"""
{prompt}

IMPORTANT: Your previous response was not valid JSON. Please respond with ONLY a valid JSON object, no explanations or additional text.

Previous invalid response: {raw_response[:200]}...

Error: {str(json_error)}

Respond with ONLY valid JSON:
"""
                    prompt = feedback_prompt
                    print(f"⚠️  Retry {attempt + 1}/{max_retries}: JSON parsing failed, retrying with feedback...")
                    continue
                else:
                    raise Exception(f"Failed to get valid JSON after {max_retries} attempts: {json_error}")
            
        except Exception as e:
            if attempt == max_retries - 1:
                raise Exception(f"Failed to call OpenRouter API: {str(e)}")
            continue
    
    raise Exception("Unexpected error in API call")


def call_openrouter_api(prompt: str, model: str = "openai/gpt-4o-mini", temperature: float = 0.1) -> str:
    """
    Call OpenRouter API with the given prompt (for non-JSON responses).
    
    Args:
        prompt: The prompt to send to the model
        model: Model name to use
        temperature: Sampling temperature (low for consistency)
        
    Returns:
        Model response text
        
    Raises:
        Exception: If API call fails
    """
    api_key = get_openrouter_api_key()
    
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
        
        return result['choices'][0]['message']['content']
        
    except Exception as e:
        raise Exception(f"Failed to call OpenRouter API: {str(e)}")


def parse_chunked_content(content: str) -> List[Dict[str, str]]:
    """
    Parse chunked markdown content and extract chunks with their contexts.
    
    Args:
        content: Full markdown content with chunk tags
        
    Returns:
        List of dictionaries with 'context' and 'content' keys
    """
    chunks = []
    
    # Find all chunk_context and chunk pairs
    pattern = r'<chunk_context>(.*?)</chunk_context>\s*<chunk>(.*?)</chunk>'
    matches = re.findall(pattern, content, re.DOTALL)
    
    for context, chunk_content in matches:
        chunks.append({
            'context': context.strip(),
            'content': chunk_content.strip()
        })
    
    if not chunks:
        # Fallback: if no chunk tags found, treat whole content as one chunk
        chunks.append({
            'context': "Document content without specific context tags",
            'content': content
        })
    
    return chunks


def load_rodeos_template() -> Dict:
    """
    Load the RODEOS JSON template structure.
    
    Returns:
        Dictionary containing the RODEOS template
        
    Raises:
        Exception: If template cannot be loaded
    """
    template_path = Path("assets/rodeos_architecture/rodeos.json")
    
    if not template_path.exists():
        raise Exception(f"RODEOS template not found: {template_path}")
    
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        raise Exception(f"Failed to load RODEOS template: {e}")


def analyze_asset_type(chunks: List[Dict[str, str]], model: str, use_remote: bool = True) -> str:
    """
    Analyze content to determine the asset type (Dataset, Model, or Service).
    
    Args:
        chunks: List of content chunks with context
        model: Model to use (OpenRouter or local Ollama)
        use_remote: Whether to use remote API via OpenRouter
        
    Returns:
        Asset type: "rodeos:Dataset", "rodeos:Model", or "rodeos:Service"
    """
    # Combine first few chunks for analysis
    combined_content = ""
    for i, chunk in enumerate(chunks[:3]):  # Use first 3 chunks for type analysis
        combined_content += f"Context {i+1}: {chunk['context']}\n"
        combined_content += f"Content {i+1}: {chunk['content'][:1000]}...\n\n"
    
    prompt = f"""
Analyze the following document content and determine which type of digital asset it describes.

ASSET TYPES:
The RODEOS semantic model defines three core asset types for representing digital and executable artifacts in robotic and automation environments. 
These asset types are designed to support semantic interoperability across domains and vendors, while remaining lightweight and easy to author.
1. "rodeos:Dataset" -  A dataset or data product refers to structured or unstructured data used for training, analysis, or monitoring purposes. This includes raw sensor logs, telemetry, inspection images, documents, or annotated datasets for machine learning. Datasets may carry labeling information for classification or regression and are described by metadata such as format, version, storage location, and access path. They form the foundational input for models and services. Further examples: Data collections, databases, files, structured/unstructured data
2. "rodeos:Model" -  A model represents any formalized knowledge or executable logic, ranging from static geometry like CAD files or URDFs to pretrained AI models and control graphs. Models may define input and output formats, reference a specific framework or runtime environment, and include deployment artifacts such as Docker images or ONNX files. They are typically consumed by services or deployed as part of a robotic system’s behavior. All files that contain description of hardware like a camera, gripper, robot, computer, cable, etc. all must be classified as model! Further examples: AI/ML models, algorithms, trained models, neural networks  
3. "rodeos:Service" - A service is an executable, hosted interface that exposes functionality over a network. It may wrap one or more models and provide access via REST, gRPC, or other protocols. Services implement logic such as pose estimation, object recognition, or skill execution, and may run on edge devices, cloud infrastructure, or within robot controllers. Metadata includes endpoint location, input/output schema, and supported protocols. Further examples: APIs, web services, software services, applications, systems

CONTENT TO ANALYZE:
{combined_content}

Based on the content, determine which single asset type best fits this document.

CRITICAL REQUIREMENTS:
- Respond with EXACTLY one of these three options (copy exactly as shown):
  rodeos:Dataset
  rodeos:Model
  rodeos:Service
- Do not include quotes, explanations, or any other text
- Do not add punctuation or newlines
- Just the exact asset type string
"""
    
    if use_remote:
        response = call_openrouter_api(prompt, model, temperature=0.1)
    else:
        response = call_model_local(prompt, model, temperature=0.1)
    asset_type = response.strip()
    
    # Validate response
    valid_types = ["rodeos:Dataset", "rodeos:Model", "rodeos:Service"]
    if asset_type not in valid_types:
        print(f"⚠️  Warning: Invalid asset type '{asset_type}', defaulting to 'rodeos:Service'")
        asset_type = "rodeos:Service"
    
    return asset_type


def extract_basic_metadata(chunks: List[Dict[str, str]], model: str, use_remote: bool = True) -> Dict[str, str]:
    """
    Extract basic metadata for dcat:Resource fields.
    
    Args:
        chunks: List of content chunks with context
        model: Model to use (OpenRouter or local Ollama)
        use_remote: Whether to use remote API via OpenRouter
        
    Returns:
        Dictionary with basic metadata fields
    """
    # Combine all content for comprehensive analysis
    full_content = ""
    for chunk in chunks:
        full_content += f"Context: {chunk['context']}\n"
        full_content += f"Content: {chunk['content']}\n\n"
    
    prompt = f"""
Extract basic metadata from the following document content for a semantic model.

CONTENT:
{full_content}

Extract the following information and respond with ONLY a valid JSON object:

{{
    "title": "Brief descriptive title",
    "type": "Type/category of the resource", 
    "description": "Clear description of what this resource is",
    "publisher": "Organization/company/author (if mentioned)",
    "keywords": "Comma-separated relevant keywords",
    "identifier": "Product number/model/ID (if mentioned)",
    "version": "Version number (if mentioned, otherwise empty)",
    "license": "License information (if mentioned, otherwise empty)",
    "contactPoint": "Contact information (if mentioned, otherwise empty)"
}}

CRITICAL REQUIREMENTS:
- Only include information that is explicitly mentioned or clearly derivable
- Use empty string for fields not found in the content
- Keep descriptions concise and factual
- Extract actual values, do not make up information
- Respond with ONLY valid JSON, no explanations or markdown formatting
- Do not include ```json``` markers or any other text
"""
    
    try:
        if use_remote:
            return call_openrouter_api_with_json_validation(prompt, model, temperature=0.1)
        else:
            return call_model_local_with_json_validation(prompt, model, temperature=0.1)
    except Exception as e:
        print(f"⚠️  Warning: Failed to extract basic metadata: {e}")
        return {
            "title": "Unknown Resource",
            "type": "Unknown",
            "description": "Resource description not available",
            "publisher": "",
            "keywords": "",
            "identifier": "",
            "version": "",
            "license": "",
            "contactPoint": ""
        }


def extract_asset_specific_metadata(chunks: List[Dict[str, str]], asset_type: str, model: str, use_remote: bool = True) -> Dict[str, str]:
    """
    Extract asset-specific metadata based on the determined asset type.
    
    Args:
        chunks: List of content chunks with context
        asset_type: The determined asset type
        model: Model to use (OpenRouter or local Ollama)
        use_remote: Whether to use remote API via OpenRouter
        
    Returns:
        Dictionary with asset-specific metadata
    """
    # Combine all content
    full_content = ""
    for chunk in chunks:
        full_content += f"Context: {chunk['context']}\n"
        full_content += f"Content: {chunk['content']}\n\n"
    
    if asset_type == "rodeos:Dataset":
        prompt = f"""
Extract dataset-specific metadata from the following content.

CONTENT:
{full_content}

Extract the following information and respond with ONLY a valid JSON object:

{{
    "dprod:informationSensitivityClassification": "Sensitivity level (public/internal/confidential/restricted)",
    "dprod:type": "Data type (tabular/computerVision/nlp/timeseries/audio/graph/other)",
    "rodeos:dataFormat": "Data format (csv/json/parquet/xml/pdf/image/etc)",
    "rodeos:isDataProduct": "true/false - is this a data product",
    "rodeos:dataTypeSize": "Size information if mentioned",
    "rodeos:dataTypeSchema": "Schema type (xsd:string/xsd:dateTime/etc)",
    "dcat:checksum": "Checksum if mentioned",
    "dcat:endpointDescription": "Description of access endpoint",
    "dcat:endpointURL": "URL to access data",
    "dcat:protocol": "Access protocol (HTTP/FTP/etc)",
    "dprod:dataProductOwner": "Owner of the data product"
}}

CRITICAL REQUIREMENTS:
- Only include information explicitly mentioned. Use empty string for unknown fields.
- Respond with ONLY valid JSON, no explanations or markdown formatting
- Do not include ```json``` markers or any other text
"""

    elif asset_type == "rodeos:Model":
        prompt = f"""
Extract model-specific metadata from the following content.

CONTENT:
{full_content}

Extract the following information and respond with ONLY a valid JSON object:

{{
    "rodeos:modelType": "Choose from: Image Generation, Video Generation, Text Generation, Language Translation, Speech Synthesis, 3D Modeling, Object Detection, Text Analysis, Image Editing, Code Generation, Question Answering, Data Visualization, Voice Cloning, Background Removal, Image Upscaling, OCR, Document Analysis, Visual QA, Image Captioning, Chatbots, Sentiment Analysis, Text Summarization, Music Generation, Medical Imaging, Financial Analysis, Game AI, Model Benchmarking, Fine Tuning Tools, Dataset Creation, Pose Estimation, Face Recognition, Anomaly Detection, Recommendation Systems, Character Animation, Style Transfer, Image Classification, Instance Segmentation, Keypoint Detection, Semantic Segmentation, Multimodal",
    "rodeos:inputShape": "Input data shape/dimensions",
    "rodeos:outputShape": "Output data shape/dimensions", 
    "rodeos:inputDataType": "Type of input data",
    "rodeos:outputDataType": "Type of output data",
    "rodeos:modelParameters": "Model parameters/configuration",
    "rodeos:framework": "ML framework (PyTorch/TensorFlow/etc)"
}}

CRITICAL REQUIREMENTS:
- Only include information explicitly mentioned. Use empty string for unknown fields.
- Choose the most appropriate modelType from the list provided.
- Respond with ONLY valid JSON, no explanations or markdown formatting
- Do not include ```json``` markers or any other text
"""

    else:  # rodeos:Service
        prompt = f"""
Extract service-specific metadata from the following content.

CONTENT:
{full_content}

Extract the following information and respond with ONLY a valid JSON object:

{{
    "rodeos:usedModels": "References to models used by this service",
    "rodeos:serviceTypeMain": "Main category of service",
    "rodeos:serviceType": "Specific type of service",
    "dcat:endpointURL": "Service endpoint URL",
    "rodeos:inputShape": "Shape of service input",
    "rodeos:inputDataType": "Input data type",
    "rodeos:outputDataType": "Output data type", 
    "dcat:endpointDescription": "Endpoint description",
    "dcat:landingPage": "Service documentation URL"
}}

CRITICAL REQUIREMENTS:
- Only include information explicitly mentioned. Use empty string for unknown fields.
- Respond with ONLY valid JSON, no explanations or markdown formatting
- Do not include ```json``` markers or any other text
"""

    try:
        if use_remote:
            return call_openrouter_api_with_json_validation(prompt, model, temperature=0.1)
        else:
            return call_model_local_with_json_validation(prompt, model, temperature=0.1)
    except Exception as e:
        print(f"⚠️  Warning: Failed to extract asset-specific metadata: {e}")
        return {}


def create_submodel_descriptions() -> Path:
    """
    Create a markdown file describing all available submodels.
    
    Returns:
        Path to the created description file
    """
    submodels_dir = Path("assets/submodels")
    description_file = submodels_dir / "submodel_descriptions.md"
    
    if description_file.exists():
        return description_file
    
    # List all JSON files in submodels directory
    json_files = list(submodels_dir.glob("*.json"))
    
    descriptions = []
    descriptions.append("# Submodel Descriptions\n")
    descriptions.append("Available submodels for RODEOS semantic model enhancement:\n")
    
    for json_file in json_files:
        try:
            with open(json_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Extract basic info from the submodel
            name = json_file.stem
            
            # Try to get description from various possible fields
            description = "Submodel for additional metadata enhancement"
            if isinstance(data, dict):
                description = data.get('description', 
                             data.get('dcterms:description', 
                             data.get('@id', name)))
            
            descriptions.append(f"- **{name}**: {description}")
            
        except Exception as e:
            descriptions.append(f"- **{json_file.stem}**: Error reading submodel ({str(e)})")
    
    content = "\n".join(descriptions)
    
    # Write description file
    with open(description_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return description_file


def select_submodel(chunks: List[Dict[str, str]], asset_type: str, model: str, use_remote: bool = True) -> Optional[Dict]:
    """
    Select the most appropriate submodel for the asset.
    
    Args:
        chunks: List of content chunks with context  
        asset_type: The determined asset type
        model: Model to use (OpenRouter or local Ollama)
        use_remote: Whether to use remote API via OpenRouter
        
    Returns:
        Dictionary containing the selected submodel or None
    """
    # Create submodel descriptions if they don't exist
    desc_file = create_submodel_descriptions()
    
    # Read submodel descriptions
    with open(desc_file, 'r', encoding='utf-8') as f:
        submodel_descriptions = f.read()
    
    # Combine content for analysis
    content_summary = ""
    for chunk in chunks[:2]:  # Use first 2 chunks
        content_summary += f"Context: {chunk['context']}\n"
        content_summary += f"Content: {chunk['content'][:800]}...\n\n"
    
    prompt = f"""
Based on the following document content and asset type, select the most appropriate submodel.

ASSET TYPE: {asset_type}

DOCUMENT CONTENT:
{content_summary}

AVAILABLE SUBMODELS:
{submodel_descriptions}

Select the single most appropriate submodel filename (without .json extension) that best fits this content and asset type.

If none of the submodels are appropriate, respond with "none".

Respond with only the submodel filename or "none".
"""
    
    if use_remote:
        response = call_openrouter_api(prompt, model, temperature=0.1)
    else:
        response = call_model_local(prompt, model, temperature=0.1)
    submodel_name = response.strip().lower()
    
    if submodel_name == "none":
        return None
    
    # Try to load the selected submodel
    submodel_path = Path(f"assets/submodels/{submodel_name}.json")
    if not submodel_path.exists():
        print(f"⚠️  Warning: Selected submodel '{submodel_name}' not found")
        return None
    
    try:
        with open(submodel_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️  Warning: Failed to load submodel '{submodel_name}': {e}")
        return None


def create_semantic_model(file_path: Path, model: str = "openai/gpt-4o-mini", use_remote: bool = True) -> Dict:
    """
    Create a complete semantic model from the chunked markdown file.
    
    Args:
        file_path: Path to the chunked markdown file
        model: Model to use (OpenRouter or local Ollama)
        use_remote: Whether to use remote API via OpenRouter
        
    Returns:
        Complete semantic model dictionary
        
    Raises:
        Exception: If model creation fails
    """
    try:
        print(f"📄 Reading chunked file: {file_path.name}")
        
        # Read the chunked content
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if not content.strip():
            raise Exception("File is empty")
        
        # Parse chunks
        print("🔍 Parsing chunks...")
        chunks = parse_chunked_content(content)
        print(f"✓ Found {len(chunks)} chunks")
        
        # Load RODEOS template
        print("📋 Loading RODEOS template...")
        rodeos_template = load_rodeos_template()
        
        # Step 1: Determine asset type
        print("🤖 Analyzing asset type...")
        asset_type = analyze_asset_type(chunks, model, use_remote)
        print(f"✓ Determined asset type: {asset_type}")
        
        # Step 2: Extract basic metadata
        print("📊 Extracting basic metadata...")
        basic_metadata = extract_basic_metadata(chunks, model, use_remote)
        print("✓ Basic metadata extracted")
        
        # Step 3: Extract asset-specific metadata
        print("🔧 Extracting asset-specific metadata...")
        asset_metadata = extract_asset_specific_metadata(chunks, asset_type, model, use_remote)
        print("✓ Asset-specific metadata extracted")
        
        # Step 4: Select submodel
        print("🎯 Selecting appropriate submodel...")
        submodel = select_submodel(chunks, asset_type, model, use_remote)
        if submodel:
            print("✓ Submodel selected")
        else:
            print("ℹ️  No suitable submodel found")
        
        # Build the semantic model
        semantic_model = {
            "dcat:Resource": {
                "dcterms:title": basic_metadata.get("title", ""),
                "dcterms:type": basic_metadata.get("type", ""),
                "dcterms:publisher": basic_metadata.get("publisher", ""),
                "dcterms:license": basic_metadata.get("license", ""),
                "dcterms:identifier": basic_metadata.get("identifier", ""),
                "dcterms:description": basic_metadata.get("description", ""),
                "dcat:version": basic_metadata.get("version", ""),
                "dcat:keyword": basic_metadata.get("keywords", ""),
                "dcat:contactPoint": basic_metadata.get("contactPoint", ""),
                "assets": {
                    asset_type: asset_metadata
                },
                "submodels": [submodel] if submodel else []
            }
        }
        
        print("✅ Semantic model created successfully")
        return semantic_model
        
    except Exception as e:
        raise Exception(f"Failed to create semantic model: {str(e)}")


def save_semantic_model(semantic_model: Dict, source_file: Path, output_dir: Path) -> Path:
    """
    Save the semantic model to a JSON file.
    
    Args:
        semantic_model: The semantic model dictionary
        source_file: Source file path for naming
        output_dir: Output directory
        
    Returns:
        Path to saved file
        
    Raises:
        Exception: If saving fails
    """
    try:
        # Create models directory
        models_dir = output_dir / "models"
        models_dir.mkdir(parents=True, exist_ok=True)
        
        # Create filename in camelCase
        base_name = source_file.stem
        # Remove common suffixes and convert to camelCase
        base_name = base_name.replace("_MISTRAL", "").replace("_DOCLING_basic", "").replace("_DOCLING_enhanced", "").replace("_CHUNKED", "")
        
        # Convert to camelCase
        parts = base_name.split('_')
        camel_case = parts[0].lower() + ''.join(word.capitalize() for word in parts[1:])
        
        output_file = models_dir / f"{camel_case}SemanticModel.json"
        
        # Save with proper formatting
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(semantic_model, f, indent=2, ensure_ascii=False)
        
        print(f"✓ Semantic model saved to: {output_file}")
        return output_file
        
    except Exception as e:
        raise Exception(f"Failed to save semantic model: {e}")


def find_chunked_files(directory: Path) -> List[Path]:
    """
    Find all chunked markdown files in the directory.
    
    Args:
        directory: Directory to search
        
    Returns:
        List of chunked markdown file paths
    """
    chunked_files = []
    if directory.exists() and directory.is_dir():
        for file_path in directory.glob("*_CHUNKED.md"):
            chunked_files.append(file_path)
    return chunked_files


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Create RODEOS semantic models from chunked markdown files",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Process single chunked file (remote by default)
  python extraction.py document_CHUNKED.md
  
  # Process with local Ollama model
  python extraction.py document_CHUNKED.md --local
  
  # Process all chunked files in assets/markdown
  python extraction.py --batch
  
  # Batch process with local model
  python extraction.py --batch --local
  
  # Use specific remote model
  python extraction.py document_CHUNKED.md --model anthropic/claude-3-haiku
  
  # Use specific local model
  python extraction.py document_CHUNKED.md --local --model llama3.2:3b
  
  # Custom output directory
  python extraction.py document_CHUNKED.md --output-dir custom_output

Remote Requirements (default):
  - OPENROUTER_API_KEY environment variable set
  - Valid OpenRouter API key with credits

Local Requirements:
  - Ollama running locally
  - A suitable LLM model installed (e.g., qwen2.5:3b, llama3.2:3b)

Prerequisites:
  - Chunked markdown files (created by context.py)
        """
    )
    
    parser.add_argument(
        'chunked_file',
        nargs='?',
        help='Path to the chunked markdown file to process'
    )
    
    parser.add_argument(
        '--batch',
        action='store_true',
        help='Process all chunked files in assets/markdown directory'
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
    if not args.batch and not args.chunked_file:
        parser.error("Must specify either a chunked markdown file or use --batch flag")
    
    # Determine processing mode and model
    use_remote = not args.local
    if args.local and args.model == 'openai/gpt-4o-mini':
        # User specified --local but didn't change model, use local default
        model = 'qwen2.5:3b'
    else:
        model = args.model
    
    try:
        # Check requirements based on processing mode
        if use_remote:
            get_openrouter_api_key()
            print(f"🌐 Using remote model: {model}")
        else:
            if not check_ollama_connection():
                raise Exception("Ollama is not running. Please start Ollama service first.")
            print(f"🏠 Using local model: {model}")
        
        output_dir = Path(args.output_dir)
        files_to_process = []
        
        if args.batch:
            # Process all chunked files in assets/markdown
            markdown_dir = Path("assets/markdown")
            if not markdown_dir.exists():
                raise Exception(f"Directory not found: {markdown_dir}")
            
            files_to_process = find_chunked_files(markdown_dir)
            if not files_to_process:
                raise Exception(f"No chunked markdown files found in {markdown_dir}")
            
            print(f"🔍 Found {len(files_to_process)} chunked files to process")
        else:
            # Process single file
            file_path = validate_markdown_file(args.chunked_file)
            if not file_path.name.endswith('_CHUNKED.md'):
                raise ValueError("File must be a chunked markdown file (*_CHUNKED.md)")
            files_to_process = [file_path]
        
        # Process files
        successful = 0
        failed = 0
        
        for file_path in files_to_process:
            try:
                print(f"\n🚀 Processing: {file_path}")
                semantic_model = create_semantic_model(file_path, model, use_remote)
                save_semantic_model(semantic_model, file_path, output_dir)
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
            print(f"📁 Output directory: {output_dir / 'models'}")
        
    except KeyboardInterrupt:
        print(f"\n⏹️  Processing interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
