from fastapi import FastAPI
from app.api.summarize import router as summarize_router

app = FastAPI(title="Role-Based Document Summarizer")

app.include_router(summarize_router)

@app.get("/health")
def health():
    return {"status": "ok"}
