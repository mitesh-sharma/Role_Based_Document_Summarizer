from app.services.ingestion.reader import read_document
from fastapi import HTTPException  
from app.services.rag_pipeline import generate_role_based_summary
from app.services.persistance_service import save_document, save_chunks, save_embeddings, check_hash
import hashlib

async def get_summary(file, role: str, detail_level: str, file_name: str | None):
    #Extract text from file
    contents = await file.read()
    if len(contents) > 5 * 1024 * 1024:
        raise HTTPException(status_code=413, detail="File too large (max 5MB).")
    text = read_document(contents, file.filename)
    if not text.strip():
        raise HTTPException(status_code=400, detail="Document is empty.")
    
    #Generate Hash
    document_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    document_id = check_hash(document_hash)
    try:
        result = generate_role_based_summary(document_text=text, role_description=role, detail_level=detail_level, document_id = document_id)
        #save document into DB
        if not document_id:
            try:
                doc_id = save_document(file_name=file_name, document_hash=document_hash)
                if result["used_rag"]:
                    save_chunks(doc_id, chunks = result["chunks"])
                    save_embeddings(doc_id, embeddings = result["embeddings"])
            except Exception as e:
                print("document couldn't save due to - ", e)
                raise
        return result
    
    except Exception as e:
        print("Inside check file persistance - ", e)
        raise
