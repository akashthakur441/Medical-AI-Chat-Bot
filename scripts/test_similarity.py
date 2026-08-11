from backend.app.services.document_service import extract_text_from_pdf
from backend.app.services.chunking_service import split_text
from backend.app.services.embedding_service import generate_embedding
from backend.app.services.similarity_service import cosine_similarity


PDF_PATH = "data/documents/medical_knowledge_base.pdf"


text = extract_text_from_pdf(PDF_PATH)
chunks = split_text(text)

query = "What are the symptoms and causes of diabetes?"

query_embedding = generate_embedding(query)

results = []

for index, chunk in enumerate(chunks):
    chunk_embedding = generate_embedding(chunk)

    score = cosine_similarity(
        query_embedding,
        chunk_embedding,
    )

    results.append((score, index, chunk))


results.sort(reverse=True, key=lambda x: x[0])


print(f"Total chunks searched: {len(results)}")

print("\nTop 3 relevant chunks:\n")

for rank, (score, index, chunk) in enumerate(results[:3], start=1):
    print(f"--- RESULT {rank} ---")
    print(f"Chunk index: {index}")
    print(f"Similarity score: {score:.4f}")
    print(chunk[:500])
    print()