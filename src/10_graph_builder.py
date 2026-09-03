from importlib import import_module

from langgraph.graph import START, StateGraph
from langgraph.prebuilt import tools_condition


State = import_module("src.07_state").State
_nodes = import_module("src.09_nodes")


graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", _nodes.chatbot)
graph_builder.add_node("tools", _nodes.tool_node)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")
