from importlib import import_module


_tool_module = import_module("src.04_tool_declaration")
_calculator_module = import_module("src.05_calculator")

tools = [
    _tool_module.wiki_tool,
    _tool_module.google_search_tool,
    _calculator_module.calculator,
]
