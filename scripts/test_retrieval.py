from backend.app.services.retrieval_service import (
    retrieve_relevant_chunks,
)


query = "What are the symptoms and causes of diabetes?"

results = retrieve_relevant_chunks(
    query=query,
    top_k=3,
)

print(f"Query: {query}")
print(f"\nRetrieved chunks: {len(results)}\n")

for rank, result in enumerate(results, start=1):
    print(f"--- RESULT {rank} ---")
    print(f"Source: {result['source']}")
    print(f"Page: {result['page']}")
    print(f"Distance: {result['distance']:.4f}")
    print(f"Text: {result['text'][:700]}")
    print("-" * 70)