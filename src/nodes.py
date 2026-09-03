from langgraph.prebuilt import ToolNode

from src.llm import llm_with_tools
from src.state import State
from src.tools import tools


def chatbot(state: State):
    """Call the LLM with the current conversation messages."""
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


tool_node = ToolNode(tools=tools)
