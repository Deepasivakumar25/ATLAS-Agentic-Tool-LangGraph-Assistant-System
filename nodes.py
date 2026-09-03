from state import State
from llm import llm_with_tools
from langgraph.prebuilt import ToolNode
from tools import tools


def chatbot(state: State):
    """Call the LLM with the current conversation messages."""
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


tool_node = ToolNode(tools=tools)
