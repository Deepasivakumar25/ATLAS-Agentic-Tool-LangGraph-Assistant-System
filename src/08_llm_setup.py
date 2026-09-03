import os

from langchain_groq import ChatGroq

from importlib import import_module


groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set.")

llm = ChatGroq(
    groq_api_key=groq_api_key,
    model_name="openai/gpt-oss-20b",
)

tools = import_module("src.06_tool_list").tools
llm_with_tools = llm.bind_tools(tools)
