# PDF to Markdown Converter

A Python tool that converts PDF documents to markdown format using the pymupdf4llm library.

## Installation

This project uses Poetry for dependency management. To install:

```bash
# Clone the repository
git clone https://github.com/hongthana/test-pymupdf4llm.git
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
│       ├── __init__.py
│       └── main.py
├── tests/
│   ├── __init__.py
│   └── data/           # Store test PDF files here
│       └── test.pdf    # Test PDF files
├── output/             # Generated markdown files
│   └── result.md
├── .gitignore
├── LICENSE
├── README.md
└── pyproject.toml
```

The project follows a standard Python package structure:
- `src/test_pymupdf4llm/`: Source code directory
- `tests/`: Test files and test data
- `output/`: Generated markdown output files
- Configuration files in root directory

## Usage

### Activate Poetry Environment

Before running the script, activate the Poetry environment:

```bash
poetry shell
```

### Running the Script

There are two ways to run the PDF converter:

1. Print output to console:
```bash
python src/test_pymupdf4llm/main.py tests/data/test.pdf
```

2. Save output to a file:
```bash
python src/test_pymupdf4llm/main.py tests/data/test.pdf -o output/result.md
```

### Command Line Options

- `pdf_path`: Path to your PDF file (required)
- `-o, --output`: Output file path (optional, defaults to 'output/result.md')

### Examples

Convert a PDF and display in console:
```bash
python src/test_pymupdf4llm/main.py tests/data/sample.pdf
```

Convert a PDF and save to a specific file:
```bash
python src/test_pymupdf4llm/main.py tests/data/sample.pdf -o output/custom_name.md
```

### Directory Setup

1. Place your PDF files in the `tests/data/` directory
2. Output files will be saved in the `output/` directory by default
3. The `output/` directory will be created automatically if it doesn't exist
