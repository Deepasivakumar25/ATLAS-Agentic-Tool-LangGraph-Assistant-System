"""Build the LangGraph graph and connect its nodes."""

from importlib import import_module

from langgraph.graph import StateGraph, START
from langgraph.prebuilt import tools_condition

State = import_module("src.07_state").State
chatbot = import_module("src.12_chatbot_node").chatbot
tool_node = import_module("src.13_toolnode").tool_node


graph_builder = StateGraph(State)

# Add nodes
 graph_builder.add_node("chatbot", chatbot)
 graph_builder.add_node("tools", tool_node)

# Add edges
 graph_builder.add_edge(START, "chatbot")
 graph_builder.add_conditional_edges("chatbot", tools_condition)
 graph_builder.add_edge("tools", "chatbot")
