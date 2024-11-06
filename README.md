# PDF to Markdown Converter

A Python tool that converts PDF documents to markdown format using the pymupdf4llm library.

## Installation

This project uses Poetry for dependency management. To install:

```bash
# Clone the repository
git clone [your-repo-url]
cd test-pymupdf4llm

# Install dependencies using Poetry
poetry install
```

## Requirements

- Python 3.9 or higher
- Poetry
- pymupdf4llm 0.0.17 or higher

## Project Structure

```
project_root/
├── src/
│   └── test_pymupdf4llm/
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── data/           # Store test PDF files here
├── output
