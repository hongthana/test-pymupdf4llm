"""
PDF to Markdown Converter

This module provides functionality to convert PDF documents to markdown format
using the pymupdf4llm library. It includes a Gradio interface for uploading
PDF files, processing them, and displaying the output as markdown along with
the conversion time.

Example:
    Run the Gradio app:
    $ poetry run python src/test_pymupdf4llm/main.py
"""

import os
import argparse
import pymupdf4llm
import gradio as gr
import time

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

def convert_pdf_to_markdown(pdf_file):
    # Ensure the output directory exists
    ensure_output_directory()
    
    # Extract the original filename without extension
    original_filename = os.path.splitext(os.path.basename(pdf_file.name))[0]
    
    # Define the output markdown file path
    output_path = f'output/{original_filename}.md'
    
    # Start timing the conversion process
    start_time = time.time()

    # Perform the conversion using pymupdf4llm
    # Assuming pymupdf4llm has a function to convert PDF to markdown
    markdown_content = pymupdf4llm.to_markdown(pdf_file.name)

    # Calculate the time taken for the conversion
    conversion_time = time.time() - start_time
    
    # Save the markdown content to the output file
    with open(output_path, 'w') as f:
        f.write(markdown_content)
    
    # Return the markdown content and the conversion time
    return f"Conversion Time: {conversion_time:.2f} seconds", markdown_content

def main():
    # Create a Gradio interface
    interface = gr.Interface(
        fn=convert_pdf_to_markdown,
        inputs=gr.File(label="Upload PDF"),
        outputs=[
            gr.Textbox(label="Conversion Time"),
            gr.Textbox(label="Markdown Output")
        ],
        title="PDF to Markdown Converter",
        description="Upload a PDF file to convert it to markdown format."
    )
    
    # Launch the Gradio app
    interface.launch()

if __name__ == "__main__":
    main()

# Example usage:
# python main.py tests/data/test.pdf                     # Print to stdout
# python main.py tests/data/test.pdf -o output/result.md # Save to file
