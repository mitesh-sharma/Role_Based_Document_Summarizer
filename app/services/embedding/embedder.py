from app.services.ai_client import client

def embed_texts(texts: list[str]) -> list[list[float]]:
    response = client.models.embed_content(
        model="models/gemini-embedding-001",
        contents=texts
    )
    return [item.values for item in response.embeddings]


def embed_chunks(chunks: list[str]) -> list[list[float]]:
    return embed_texts(chunks)


def embed_query(query: str) -> list[float]:
    return embed_texts([query])[0]
