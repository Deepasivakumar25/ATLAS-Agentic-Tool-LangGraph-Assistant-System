"""Compile the graph with in-memory conversation memory."""

from importlib import import_module

from langgraph.checkpoint.memory import MemorySaver


graph_builder = import_module("src.14_graph_builder").graph_builder


memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)
