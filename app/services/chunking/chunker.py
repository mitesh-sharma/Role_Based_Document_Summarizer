def chunk_text(text: str, max_words: int) -> list[str]:
    if max_words <= 0:
        raise ValueError("max_words must be greater than 0")

    words = text.split()   # splits on all whitespace safely
    chunks = []

    for i in range(0, len(words), max_words):
        chunk_words = words[i:i + max_words]
        chunk = " ".join(chunk_words)
        chunks.append(chunk)

    return chunks
