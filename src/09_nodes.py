from importlib import import_module

from langgraph.prebuilt import ToolNode


State = import_module("src.07_state").State
llm_with_tools = import_module("src.08_llm_setup").llm_with_tools
tools = import_module("src.06_tool_list").tools


def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


tool_node = ToolNode(tools=tools)
