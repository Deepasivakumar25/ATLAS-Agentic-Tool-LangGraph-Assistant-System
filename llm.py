from langchain_groq import ChatGroq

from config import GROQ_API_KEY
from tools import tools


llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="openai/gpt-oss-20b",
)

llm_with_tools = llm.bind_tools(tools)
