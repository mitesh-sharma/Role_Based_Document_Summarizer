from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    DEBUG = os.getenv("DEBUG") == "True"

settings = Settings()
