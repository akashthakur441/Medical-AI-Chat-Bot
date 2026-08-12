def split_text(
    text: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> list[str]:
    if not text.strip():
        return []

    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        start += chunk_size - chunk_overlap

    return chunks


def split_pages_into_chunks(
    pages: list[dict],
    source: str,
    chunk_size: int = 1000,
    chunk_overlap: int = 200,
) -> list[dict]:

    all_chunks = []

    for page_data in pages:
        page_number = page_data["page"]
        text = page_data["text"]

        if not text.strip():
            continue

        page_chunks = split_text(
            text=text,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

        for chunk in page_chunks:
            all_chunks.append(
                {
                    "text": chunk,
                    "source": source,
                    "page": page_number,
                }
            )

    return all_chunks