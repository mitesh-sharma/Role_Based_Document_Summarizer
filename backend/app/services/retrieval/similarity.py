def retrieve_top_k_chunks(query_embedding: list[float], chunk_embeddings: list[list[float]], chunks: list[str], k: int) -> list[str]:
    
    mod_query_embeddings = 0
    cos_chunk_list = []
    for value in query_embedding:
        mod_query_embeddings += value**2
    mod_query_embeddings **= 0.5
    
    for i, embedding in enumerate(chunk_embeddings):
        dot_product = 0.0
        mod_chunk_embeddings = 0
        for j, value in enumerate(embedding):
            dot_product += query_embedding[j]*value
            mod_chunk_embeddings += value**2
        mod_chunk_embeddings **= 0.5
        cos = dot_product/(mod_chunk_embeddings*mod_query_embeddings)
        cos_chunk_list.append([cos, chunks[i]])
    
    cos_chunk_list.sort(key=lambda x: x[0], reverse=True)

    k = min(k, len(cos_chunk_list))
    return [cos_chunk_list[i][1] for i in range(k)]