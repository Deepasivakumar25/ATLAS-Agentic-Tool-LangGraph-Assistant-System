from langgraph.prebuilt import ToolNode

from src.llm import llm
from src.state import State
from src.tools import tools


# Bind the LLM to the declared tools.
llm_with_tools = llm.bind_tools(tools)


# 4. Node creation

def chatbot(state: State):
    """Call the LLM with the current conversation messages."""
    response = llm_with_tools.invoke(state["messages"])
    return {"messages": [response]}


tool_node = ToolNode(tools=tools)
