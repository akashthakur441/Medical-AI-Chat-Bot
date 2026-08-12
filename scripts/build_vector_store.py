from pathlib import Path

from backend.app.services.document_service import extract_pages_from_pdf
from backend.app.services.chunking_service import split_pages_into_chunks
from backend.app.services.embedding_service import generate_embedding
from backend.app.services.vector_store import (
    create_faiss_index,
    save_faiss_index,
    save_metadata,
)


DOCUMENTS_DIR = Path("data/documents")


def main():
    pdf_files = sorted(DOCUMENTS_DIR.glob("*.pdf"))

    if not pdf_files:
        print("No PDF files found in data/documents/")
        return

    print(f"Found {len(pdf_files)} PDF file(s).")

    all_chunks = []

    for pdf_path in pdf_files:
        print("\n" + "=" * 60)
        print(f"Processing: {pdf_path.name}")
        print("=" * 60)

        pages = extract_pages_from_pdf(str(pdf_path))

        print(f"Pages with text: {len(pages)}")

        chunks = split_pages_into_chunks(
            pages=pages,
            source=pdf_path.name,
        )

        print(f"Chunks created: {len(chunks)}")

        all_chunks.extend(chunks)

    print("\n" + "=" * 60)
    print(f"Total chunks from all PDFs: {len(all_chunks)}")
    print("=" * 60)

    print("\nGenerating embeddings...")

    embeddings = []

    for index, chunk in enumerate(all_chunks, start=1):
        embedding = generate_embedding(chunk["text"])

        embeddings.append(embedding)

        print(f"Embedded {index}/{len(all_chunks)}")

    print("\nCreating FAISS index...")

    faiss_index = create_faiss_index(embeddings)

    save_faiss_index(faiss_index)

    save_metadata(all_chunks)

    print("\nFAISS vector store created successfully.")
    print("Metadata saved successfully.")


if __name__ == "__main__":
    main()