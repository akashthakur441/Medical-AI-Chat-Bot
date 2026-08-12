import json
from pathlib import Path

import faiss
import numpy as np


VECTOR_STORE_DIR = Path("data/vector_store")
INDEX_PATH = VECTOR_STORE_DIR / "medical.index"
METADATA_PATH = VECTOR_STORE_DIR / "metadata.json"


def create_faiss_index(embeddings: list[list[float]]) -> faiss.Index:
    vectors = np.array(embeddings, dtype="float32")

    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)

    index.add(vectors)

    return index


def save_faiss_index(index: faiss.Index) -> None:
    VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)

    faiss.write_index(index, str(INDEX_PATH))


def load_faiss_index() -> faiss.Index:
    return faiss.read_index(str(INDEX_PATH))


def save_metadata(metadata: list[dict]) -> None:
    VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)

    with open(METADATA_PATH, "w", encoding="utf-8") as file:
        json.dump(metadata, file, ensure_ascii=False, indent=2)


def load_metadata() -> list[dict]:
    with open(METADATA_PATH, "r", encoding="utf-8") as file:
        return json.load(file)