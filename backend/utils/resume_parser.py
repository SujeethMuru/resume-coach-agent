import fitz #PyMuPDF

def extract_text_from_pdf(file_stream) -> str:
    """
    Extracts text from a PDF file stream

    Args:
        file_stream: A file-like object (from Flask request.files['resume'])

    Returns:
        str: Extracted plain text from the PDF
    """
    try:
        with fitz.open(stream=file_stream.read(), filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
        return text.strip()
    except Exception as e:
        return f"Failed to extract text from PDF: {e}"