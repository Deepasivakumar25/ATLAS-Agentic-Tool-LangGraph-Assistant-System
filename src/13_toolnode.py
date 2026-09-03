"""ToolNode and conditional routing from the notebook."""

from importlib import import_module

from langgraph.prebuilt import ToolNode, tools_condition


tools = import_module("src.06_tool_list").tools


tool_node = ToolNode(tools=tools)
