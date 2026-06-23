from fastapi import APIRouter, UploadFile, File, Form
from fastapi import HTTPException  

from app.services.get_summary import get_summary
from app.schema.summary_model import SummaryResponse

import time

router = APIRouter()

@router.post("/summarize", response_model=SummaryResponse)
async def summarize(
    file: UploadFile = File(...),
    role: str = Form(...),
    detail_level: str = Form(...)
):
    #start time for latency calculation
    start = time.time()
    
    try:
        #Summarizing the file
        result = await get_summary(file=file, role=role, detail_level=detail_level, file_name = file.filename)
        
        return SummaryResponse(
        summary=result["summary"],
        document_word_count=result["document_word_count"],
        target_words=result["target_words"],
        actual_words=result["actual_words"],
        role=role,
        detail_level=detail_level,
        latency_ms = int((time.time() - start) * 1000),
        password = 'www'
        )

    except HTTPException:
        raise
    
    except Exception as e:
        print(e)
        raise HTTPException(status_code=503, detail="AI service temporarily unavailable.")

    

