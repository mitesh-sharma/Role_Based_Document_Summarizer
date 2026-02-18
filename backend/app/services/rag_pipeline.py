from app.services.chunking.chunker import chunk_text
from app.services.embedding.embedder import embed_chunks, embed_query
from app.services.retrieval.similarity import retrieve_top_k_chunks
from app.services.summarization.generation import summarize
from app.helpers.calculate_max_words import calculate_max_words

def generate_role_based_summary(
    document_text: str,
    role_description: str,
    detail_level: str
):
    k = 6
    chunk_size = 600

    if not document_text.strip():
        raise ValueError("Document is empty")

    # Word count
    doc_words = len(document_text.split())

    # Calculate target length
    max_words = calculate_max_words(doc_words, detail_level)

    # If small document, skip RAG
    if doc_words < 1000:
        context = document_text
    else:
        chunks = chunk_text(document_text, chunk_size)
        chunk_embeddings = embed_chunks(chunks)

        query = f"Role description: {role_description}"
        query_embedding = embed_query(query)

        top_k_chunks = retrieve_top_k_chunks(
            query_embedding,
            chunk_embeddings,
            chunks,
            k
        )

        context = "\n\n".join(top_k_chunks)

    summary = summarize(        
        context=context,
        role_description=role_description,
        max_words=max_words
    )

    return {
        "summary": summary,
        "document_word_count": doc_words,
        "target_words": max_words,
        "actual_words": len(summary.split()),
        "detail_level": detail_level,
        "role": role_description
    }
