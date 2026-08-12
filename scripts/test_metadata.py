from pathlib import Path

from backend.app.services.document_service import extract_pages_from_pdf
from backend.app.services.chunking_service import split_pages_into_chunks


PDF_PATH = "data/documents/medical_knowledge_base.pdf"


pdf_path = Path(PDF_PATH)

pages = extract_pages_from_pdf(PDF_PATH)

chunks = split_pages_into_chunks(
    pages=pages,
    source=pdf_path.name,
)

print(f"Total pages with text: {len(pages)}")
print(f"Total chunks: {len(chunks)}")

print("\n--- FIRST 3 CHUNKS ---\n")

for index, chunk in enumerate(chunks[:3], start=1):
    print(f"CHUNK {index}")
    print(f"Source: {chunk['source']}")
    print(f"Page: {chunk['page']}")
    print(f"Text: {chunk['text'][:500]}")
    print("-" * 60)