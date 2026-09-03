from langchain_groq import ChatGroq

from src.config import GROQ_API_KEY


# LLM declaration
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="openai/gpt-oss-20b",
)
