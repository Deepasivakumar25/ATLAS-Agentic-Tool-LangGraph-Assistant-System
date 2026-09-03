from importlib import import_module

_tools = import_module("src.08_tool_declaration")
_calculator = import_module("src.09_calculator")

tools = [_tools.wiki_tool, _tools.google_search_tool, _calculator.calculator]
