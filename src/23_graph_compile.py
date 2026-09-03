from importlib import import_module

MemorySaver = import_module("src.02_imports").MemorySaver
graph_builder = import_module("src.22_graph_builder").graph_builder

memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)
