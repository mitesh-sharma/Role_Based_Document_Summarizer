from app.services.chunking.chunker import chunk_text
from app.services.embedding.embedder import embed_chunks, embed_query
from app.services.retrieval.similarity import retrieve_top_k_chunks
from app.services.summarization.generation import summarize
from app.helpers.calculate_max_words import calculate_max_words
from app.services.persistance_service import save_chunks, get_chunks, save_embeddings, get_embeddings, save_summary, get_summary

def generate_role_based_summary(
    document_text: str,
    role_description: str,
    detail_level: str,
    document_id: int | None
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
    if doc_words < 100:
        try:
            context = document_text
            summary = summarize(        
                    context=context,
                    role_description=role_description,
                    max_words=max_words
                )
            #save summary
            save_summary()
            return {
                "summary": summary,
                "chunks": [],
                "embeddings": [],
                "document_word_count": doc_words,
                "target_words": max_words,
                "actual_words": len(summary.split()),
                "used_rag": False
            }
        except Exception as e:
            raise Exception(f"Error during processing: {str(e)}")
        
    #If large document, implement RAG
    else:
        try:
            chunks = get_chunks(document_id)
            print("chunks - ", chunks)
            if(not chunks):
                chunks = chunk_text(document_text, chunk_size)
            chunk_embeddings = get_embeddings(document_id)
            if(not chunk_embeddings):
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
            #save summary into DB
            save_summary()
            return {
                "summary": summary,
                "chunks": chunks,
                "embeddings": chunk_embeddings,
                "document_word_count": doc_words,
                "target_words": max_words,
                "actual_words": len(summary.split()),
                "used_rag": True
            }
        except Exception as e:
            raise Exception(f"Error during processing: {str(e)}")

