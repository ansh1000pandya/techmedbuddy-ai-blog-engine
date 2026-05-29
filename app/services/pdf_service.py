try:
    import fitz
except ImportError:
    fitz = None


def extract_text_from_pdf(pdf_path):

    if fitz is None:
        return "PyMuPDF not installed."

    doc = fitz.open(pdf_path)

    text = ""

    for page in doc:
        text += page.get_text()

    return text