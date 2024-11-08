# PDF to Markdown Converter

This application allows you to convert PDF documents to markdown format using the `pymupdf4llm` library. It features a Gradio interface for easy file uploads and conversion, displaying both the markdown content and the time taken for the conversion.

## Features

- Convert PDF files to markdown format.
- Upload PDF files through a Gradio web interface.
- Automatically saves the output markdown file using the original filename with a `.md` extension in the `output` folder.
- Displays the markdown content and the conversion time directly on the Gradio interface.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd test-pymupdf4llm
   ```

2. Install the dependencies:
   ```bash
   poetry install
   ```

3. Ensure you have the required Python version:
   - Python 3.10 or higher

## Usage

1. Run the application:
   ```bash
   poetry run python src/test_pymupdf4llm/main.py
   ```

2. Open the Gradio interface in your web browser.

3. Upload a PDF file to convert it to markdown format.

4. The markdown content and conversion time will be displayed on the interface, and a file will be saved in the `output` directory.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries, please contact the author at thanawat.rn@gmail.com.
