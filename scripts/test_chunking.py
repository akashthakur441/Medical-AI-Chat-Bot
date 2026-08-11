from backend.app.services.document_service import extract_text_from_pdf
from backend.app.services.chunking_service import split_text


PDF_PATH = "data/documents/medical_knowledge_base.pdf"


text = extract_text_from_pdf(PDF_PATH)

chunks = split_text(text)

print(f"Total characters: {len(text)}")
print(f"Total chunks: {len(chunks)}")

for index, chunk in enumerate(chunks[:3], start=1):
    print(f"\n--- CHUNK {index} ---\n")
    print(chunk)