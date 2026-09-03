"""Bind the declared tools to the LLM."""

from importlib import import_module

llm = import_module("src.09_llm_setup").llm
tools = import_module("src.06_tool_list").tools


llm_with_tools = llm.bind_tools(tools)
