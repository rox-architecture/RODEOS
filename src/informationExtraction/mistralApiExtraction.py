#!/usr/bin/env python3
"""
Mistral AI OCR CLI Application

This module provides a command-line interface for processing PDF files using
Mistral AI's OCR capabilities following the official example pattern.

Note: The Mistral AI OCR API converts PDF content to markdown format but does
not extract or provide access to images from the PDF. Image references in the 
output markdown (e.g., ![img-0.jpeg](img-0.jpeg)) are placeholders indicating
where images existed in the original document.
"""

import argparse
import os
import sys
from pathlib import Path
from typing import Optional

from mistralai import Mistral


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


def get_api_key() -> str:
    """
    Get the Mistral API key from environment variables.
    
    Returns:
        The API key string
        
    Raises:
        ValueError: If API key is not found
    """
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError(
            "MISTRAL_API_KEY environment variable not found. "
            "Please set it with your Mistral AI API key."
        )
    return api_key


def process_pdf_with_ocr(client: Mistral, pdf_path: Path) -> str:
    """
    Process OCR on a local PDF file using Mistral AI.
    
    Args:
        client: Initialized Mistral client
        pdf_path: Path to the local PDF file
        
    Returns:
        OCR result text formatted as markdown
        
    Raises:
        Exception: If OCR processing fails
    """
    try:
        print(f"Processing OCR for: {pdf_path.name}")
        
        # For local files, we need to upload first and get a signed URL
        with open(pdf_path, "rb") as pdf_file:
            uploaded_pdf = client.files.upload(
                file={
                    "file_name": pdf_path.name,
                    "content": pdf_file,
                },
                purpose="ocr"
            )
        
        print(f"Upload successful. File ID: {uploaded_pdf.id}")
        
        # Get signed URL
        signed_url = client.files.get_signed_url(file_id=uploaded_pdf.id)
        
        # Process OCR using the signed URL
        ocr_response = client.ocr.process(
            model="mistral-ocr-latest",
            document={
                "type": "document_url",
                "document_url": signed_url.url,
            }
        )
        
        print("OCR processing completed successfully")
        
        # Extract content using the proper response structure (following official example)
        if hasattr(ocr_response, 'pages') and ocr_response.pages:
            # Format the content like in the official example
            content = "\n\n".join([
                f"### Page {i+1}\n{ocr_response.pages[i].markdown}" 
                for i in range(len(ocr_response.pages))
            ])
            
            # Cleanup the uploaded file
            try:
                client.files.delete(file_id=uploaded_pdf.id)
                print(f"Cleaned up uploaded file: {uploaded_pdf.id}")
            except Exception as e:
                print(f"Warning: Failed to cleanup uploaded file: {str(e)}")
            
            return content
        else:
            raise Exception("No pages found in OCR response")
            
    except Exception as e:
        raise Exception(f"Failed to process OCR: {str(e)}")


def process_pdf_from_url(client: Mistral, pdf_url: str) -> str:
    """
    Process OCR on a PDF from URL using Mistral AI (following official example).
    
    Args:
        client: Initialized Mistral client
        pdf_url: URL to the PDF file
        
    Returns:
        OCR result text formatted as markdown
        
    Raises:
        Exception: If OCR processing fails
    """
    try:
        print(f"Processing OCR for URL: {pdf_url}")
        
        # Process directly from URL (like in official example)
        ocr_response = client.ocr.process(
            model="mistral-ocr-latest",
            document={
                "type": "document_url",
                "document_url": pdf_url
            }
        )
        
        print("OCR processing completed successfully")
        
        # Extract content using the proper response structure
        if hasattr(ocr_response, 'pages') and ocr_response.pages:
            return "\n\n".join([
                f"### Page {i+1}\n{ocr_response.pages[i].markdown}" 
                for i in range(len(ocr_response.pages))
            ])
        else:
            raise Exception("No pages found in OCR response")
            
    except Exception as e:
        raise Exception(f"Failed to process OCR: {str(e)}")


def save_markdown_result(content: str, source_name: str, output_dir: Path) -> Path:
    """
    Save the extracted markdown content to a file in the markdown directory.
    
    Note: Image references in the markdown (e.g., ![img-0.jpeg](img-0.jpeg)) 
    are placeholders from Mistral AI's OCR. The current Mistral AI OCR API 
    does not provide functionality to extract and save actual images from PDFs.
    These references indicate where images existed in the original document.
    
    Args:
        content: The markdown content to save
        source_name: Base name for the output file (without extension)
        output_dir: Base output directory (will create 'markdown' subdirectory)
        
    Returns:
        Path to the saved markdown file
        
    Raises:
        OSError: If file creation fails
    """
    try:
        # Create markdown subdirectory instead of using the PDF directory
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Create output filename
        output_file = output_dir / f"{source_name}_MISTRAL.md"
        
        # Write content to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"✓ Markdown saved to: {output_file}")
        return output_file
        
    except Exception as e:
        raise OSError(f"Failed to save markdown file: {e}")


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="Process PDF files using Mistral AI OCR",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python mistralApiExtraction.py document.pdf
  python mistralApiExtraction.py /path/to/document.pdf
  python mistralApiExtraction.py --url https://example.com/document.pdf
  python mistralApiExtraction.py --output-dir custom_output document.pdf

Environment Variables:
  MISTRAL_API_KEY    Required. Your Mistral AI API key.
        """
    )
    
    # Create mutually exclusive group for file vs URL
    source_group = parser.add_mutually_exclusive_group(required=True)
    source_group.add_argument(
        'pdf_file', 
        nargs='?',
        help='Path to the PDF file to process'
    )
    source_group.add_argument(
        '--url',
        help='URL to the PDF file to process'
    )
    
    parser.add_argument(
        '--output-dir',
        default='assets/markdown',
        help='Output directory for markdown files (default: assets/pdf)'
    )
    
    args = parser.parse_args()
    
    try:
        # Get API key
        api_key = get_api_key()
        output_dir = Path(args.output_dir)
        
        # Initialize Mistral client
        client = Mistral(api_key=api_key)
        
        if args.url:
            # Process PDF from URL
            print(f"Starting OCR processing for URL: {args.url}")
            ocr_result = process_pdf_from_url(client, args.url)
            source_name = "url_ocr_result"  # Simple name for URL-based processing
            
        else:
            # Process local PDF file
            pdf_path = validate_pdf_file(args.pdf_file)
            print(f"Starting OCR processing for: {pdf_path}")
            ocr_result = process_pdf_with_ocr(client, pdf_path)
            source_name = pdf_path.stem  # Get filename without extension
        
        # Save result
        output_path = save_markdown_result(ocr_result, source_name, output_dir)
        
        # Display success message with correct source info
        display_source = args.url if args.url else str(pdf_path)
        print(f"\n✅ Successfully processed {display_source}")
        print(f"📄 Output saved to: {output_path}")
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()