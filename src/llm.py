from langchain_groq import ChatGroq

from src.config import GROQ_API_KEY
from src.tools import tools


# LLM declaration
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="openai/gpt-oss-20b",
)


# Bind tools to the LLM
llm_with_tools = llm.bind_tools(tools)
