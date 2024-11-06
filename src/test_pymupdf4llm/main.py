"""
PDF to Markdown Converter

This module provides functionality to convert PDF documents to markdown format
using the pymupdf4llm library. It includes command-line interface support
for processing PDF files and saving the output as markdown.

Example:
    $ python main.py tests/data/test.pdf
    $ python main.py tests/data/test.pdf -o output/result.md
"""

import os
import argparse
from pymupdf4llm.document import Document

def ensure_output_directory() -> None:
    """Create the output directory if it doesn't exist.
    
    Creates a directory named 'output' in the project root to store
    generated markdown files. If the directory already exists,
    this function will do nothing.
    
    Returns:
        None
    
    Raises:
        OSError: If directory creation fails due to permissions or other OS issues.
    """
    os.makedirs('output', exist_ok=True)

def main() -> None:
    """Process a PDF file and convert it to markdown format.
    
    This function serves as the main entry point for the PDF to markdown converter.
    It handles command-line argument parsing and orchestrates the conversion process.
    
    Command-line Arguments:
        pdf_path: Path to the input PDF file
        -o, --output: Optional path for the output markdown file (default: output/result.md)
    
    Returns:
        None
    
    Raises:
        FileNotFoundError: If the input PDF file doesn't exist
        PermissionError: If there are permission issues with reading/writing files
        Exception: For other unexpected errors during processing
    
    Example:
        To convert a PDF and print to stdout:
            $ python main.py tests/data/test.pdf
        
        To convert a PDF and save to a file:
            $ python main.py tests/data/test.pdf -o output/result.md
    """
    parser = argparse.ArgumentParser(
        description='Convert PDF documents to markdown format'
    )
    parser.add_argument(
        'pdf_path',
        help='Path to the PDF file to be converted'
    )
    parser.add_argument(
        '-o', '--output',
        help='Output markdown file path (default: output/result.md)',
        default='output/result.md'
    )
    
    args = parser.parse_args()
    
    ensure_output_directory()
    
    try:
        doc = Document(args.pdf_path)
        result = doc.to_markdown()
        
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(result)
        else:
            print(result)
            
    except FileNotFoundError:
        print(f"Error: The file '{args.pdf_path}' was not found.")

if __name__ == "__main__":
    main()

# Example usage:
# python main.py tests/data/test.pdf                     # Print to stdout
# python main.py tests/data/test.pdf -o output/result.md # Save to file
