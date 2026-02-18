# app/services/ai_client.py

from google import genai
from app.core.config import settings

if not settings.GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not set in environment variables.")

client = genai.Client(api_key=settings.GOOGLE_API_KEY)
