"""Chatbot node from the notebook."""

from importlib import import_module

State = import_module("src.07_state").State
llm_with_tools = import_module("src.10_bind_tools").llm_with_tools


def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}
