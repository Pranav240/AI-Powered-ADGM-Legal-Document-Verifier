# document_parser.py
from docx import Document
import logging

def parse_docx(path):
    """
    Extracts and returns text from a .docx file.
    If the file cannot be opened or is invalid, logs a warning and returns empty string.
    """
    try:
        doc = Document(path)
    except Exception as e:
        logging.warning(f"Failed to open {path}: {e}")
        return ""  # Return empty string on failure

    full_text = []
    for para in doc.paragraphs:
        if para.text.strip():  # ignore empty lines
            full_text.append(para.text.strip())

    return "\n".join(full_text)
