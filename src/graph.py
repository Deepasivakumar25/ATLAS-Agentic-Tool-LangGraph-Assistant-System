from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, StateGraph
from langgraph.prebuilt import tools_condition

from src.nodes import chatbot, tool_node
from src.state import State


# 5. Graph and edge creation
graph_builder = StateGraph(State)

graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)

# Start -> Chatbot
# Chatbot -> Tools when the LLM requests a tool
# Chatbot -> End when no tool is requested
# Tools -> Chatbot after tool execution
graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")


# Compile the graph with in-memory conversation history.
memory = MemorySaver()
graph = graph_builder.compile(checkpointer=memory)
