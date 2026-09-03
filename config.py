import os


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

if not SERPER_API_KEY:
    raise ValueError("SERPER_API_KEY environment variable is not set.")

os.environ["SERPER_API_KEY"] = SERPER_API_KEY
