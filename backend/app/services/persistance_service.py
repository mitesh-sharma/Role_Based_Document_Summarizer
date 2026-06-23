from app.db.session import SessionLocal
from app.db.models.document import Document
from app.db.models.chunk import Chunk

#Check Hash
def check_hash(document_hash: str):
    session = SessionLocal()
    try:
        document = session.query(Document).filter(Document.document_hash == document_hash).first()
        if document:
            return document.id
        return None
    finally:
        session.close()

#Save document
def save_document(file_name: str, document_hash: str) -> int:
    session = SessionLocal()
    try:
        document = Document(
            file_name=file_name,
            document_hash=document_hash
        )
        session.add(document)
        session.commit()
        
        return document.id
    except Exception:
        session.rollback()
        raise
    finally:    
        session.close()

def save_chunks(document_id: int, chunks: list[str]):
    session = SessionLocal()
    try:
        for index, c in enumerate(chunks):
            chunk = Chunk(
                document_id=document_id,
                chunk_index=index,
                chunk_text=c
            )
            session.add(chunk)
        
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:    
        session.close()
        

def get_chunks(document_id: int) -> list[str]:
    session = SessionLocal()
    try:
        chunks = session.query(Chunk).filter(Chunk.document_id == document_id).order_by(Chunk.chunk_index).all()
        if chunks:
            return [chunk.chunk_text for chunk in chunks]
        return None
    finally:
        session.close()
    

def save_embeddings(document_id: int, embeddings: list[str]):
    pass

def get_embeddings(document_id: int | None):
    pass

def save_summary():
    pass

def get_summary():
    pass