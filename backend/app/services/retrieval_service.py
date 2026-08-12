import numpy as np

from backend.app.services.embedding_service import generate_embedding
from backend.app.services.vector_store import (
    load_faiss_index,
    load_metadata,
)


def retrieve_relevant_chunks(
    query: str,
    top_k: int = 3,
) -> list[dict]:

    index = load_faiss_index()
    metadata = load_metadata()

    query_embedding = generate_embedding(query)

    query_vector = np.array(
        [query_embedding],
        dtype="float32",
    )

    distances, indices = index.search(
        query_vector,
        top_k,
    )

    results = []

    for distance, index_position in zip(
        distances[0],
        indices[0],
    ):
        if index_position < 0:
            continue

        chunk = metadata[int(index_position)].copy()

        chunk["distance"] = float(distance)

        results.append(chunk)

    return results