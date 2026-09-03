from importlib import import_module

llm = import_module("src.16_llm_setup").llm
tools = import_module("src.11_tool_list").tools

llm_with_tools = llm.bind_tools(tools)
