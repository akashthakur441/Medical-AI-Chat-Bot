from backend.app.services.embedding_service import generate_embedding


text = "Diabetes is a medical condition that affects blood sugar levels."

embedding = generate_embedding(text)

print("Embedding type:", type(embedding))
print("Embedding dimensions:", len(embedding))
print("First 10 values:", embedding[:10])