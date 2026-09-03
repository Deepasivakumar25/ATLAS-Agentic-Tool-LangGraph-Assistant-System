from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START
from langgraph.prebuilt import tools_condition

from state import State
from nodes import chatbot, tool_node


# Build graph
graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)

# Routing: chatbot -> tools when the LLM requests a tool.
graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")


# Add in-memory conversation persistence.
memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)
