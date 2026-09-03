"""Collect all tools that can be selected by the LLM."""

from importlib import import_module

wiki_tool = import_module("src.04_tool_declaration").wiki_tool
google_search_tool = import_module("src.04_tool_declaration").google_search_tool
calculator = import_module("src.05_calculator").calculator


tools = [wiki_tool, google_search_tool, calculator]
