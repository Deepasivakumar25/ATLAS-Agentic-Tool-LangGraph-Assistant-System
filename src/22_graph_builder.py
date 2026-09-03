from importlib import import_module

StateGraph = import_module("src.13_graph_imports").StateGraph
START = import_module("src.13_graph_imports").START
tools_condition = import_module("src.20_toolnode_imports").tools_condition
State = import_module("src.12_state").State
chatbot = import_module("src.19_chatbot_node").chatbot
tool_node = import_module("src.21_toolnode").tool_node


graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("tools", tool_node)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", tools_condition)
graph_builder.add_edge("tools", "chatbot")
