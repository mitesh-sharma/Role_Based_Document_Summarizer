from fastapi import HTTPException
from .pdf_reader import read_pdf
from .docx_reader import read_docx
from .image_reader import read_image

def read_document(file_bytes: bytes, filename: str) -> str:
    if filename.endswith(".txt"):
        return file_bytes.decode("utf-8")
    elif filename.endswith(".pdf"):
        return read_pdf(file_bytes)
    elif filename.endswith(".docx"):
        return read_docx(file_bytes)
    elif filename.endswith((".png", ".jpg", ".jpeg")):
        return read_image(file_bytes)
    else:
        raise HTTPException(status_code=400, detail="Unsupported file format.")