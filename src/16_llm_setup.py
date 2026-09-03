from importlib import import_module

ChatGroq = import_module("src.14_llm_import").ChatGroq
groq_api_key = import_module("src.15_groq_api_key").groq_api_key

llm = ChatGroq(groq_api_key=groq_api_key, model_name="openai/gpt-oss-20b")
