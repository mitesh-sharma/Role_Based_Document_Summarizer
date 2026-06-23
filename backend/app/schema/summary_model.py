from pydantic import BaseModel

class SummaryResponse(BaseModel):
    summary: str
    document_word_count: int
    target_words: int
    actual_words: int
    role: str
    detail_level: str
    latency_ms: int