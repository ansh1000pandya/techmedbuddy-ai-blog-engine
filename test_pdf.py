from app.services.pdf_service import extract_text_from_pdf

pdf_path = "sample_paper.pdf"

text = extract_text_from_pdf(pdf_path)

print(text[:5000])