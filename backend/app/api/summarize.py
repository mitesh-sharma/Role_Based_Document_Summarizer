from fastapi import APIRouter, UploadFile, File, Form
from app.services.rag_pipeline import generate_role_based_summary

router = APIRouter()

@router.post("/summarize")
async def summarize(
    file: UploadFile = File(...),
    role: str = Form(...),
    detail_level: str = Form(...)
):
    contents = await file.read()
    text = contents.decode("utf-8")

    result = generate_role_based_summary(
        document_text=text,
        role_description=role,
        detail_level=detail_level
    )

    return result


