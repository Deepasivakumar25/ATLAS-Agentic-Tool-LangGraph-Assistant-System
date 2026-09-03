from importlib import import_module

ToolNode = import_module("src.20_toolnode_imports").ToolNode
tools = import_module("src.11_tool_list").tools

tool_node = ToolNode(tools=tools)
