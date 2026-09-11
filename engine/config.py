import os


ASSISTANT_NAME = "mushaki"

from dotenv import load_dotenv

load_dotenv()

LLM_KEY = os.getenv("GEMINI_API_KEY")
