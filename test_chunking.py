from app.services.pdf_service import extract_text_from_pdf
from app.services.chunking_service import chunk_text

text = extract_text_from_pdf("sample_paper.pdf")

chunks = chunk_text(text)

print(f"Total Chunks: {len(chunks)}")

print("\nFIRST CHUNK:\n")

print(chunks[0][:2000])