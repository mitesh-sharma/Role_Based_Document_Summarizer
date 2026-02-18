from fastapi import APIRouter, UploadFile, File, Form
from pathlib import Path
import uuid
from app.services.rag_pipeline import generate_role_based_summary
from app.helpers.calculate_max_words import calculate_max_words

router = APIRouter()

UPLOAD_DIR = Path("data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), role: str = Form(...), detail_level: str = Form(...)):
    document_id = str(uuid.uuid4())
    file_path = UPLOAD_DIR / f"{document_id}_{file.filename}"

    with open(file_path, "wb") as f: 
        contents = await file.read()
        f.write(contents)
    
    length = 0
    if file_path.endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            length = len(text.split())
    print('length of file - ', length, f'\n')

    max_words = calculate_max_words(length, detail_level)
    result = generate_role_based_summary(
        max_words,
        document=text,
        role=role,
        detail_level=detail_level
    )
    
    return {
        "Result" : result,
        "filename": file.filename,
        "stored_path": str(file_path)   
    }
