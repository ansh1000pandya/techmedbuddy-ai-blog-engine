import os
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_MODEL = "gemini-2.0-flash"
GROQ_MODEL = "llama-3.1-8b-instant"
UNSPLASH_ACCESS_KEY = os.getenv("UNSPLASH_ACCESS_KEY")

MAX_TOKENS = 4000
TEMPERATURE = 0.7
