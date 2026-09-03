from langgraph.prebuilt import ToolNode

from src.llm import llm
from src.state import State
from src.tools import tools


# Bind the LLM to the declared tools
llm_with_tools = llm.bind_tools(tools)


# Node creation

def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}


tool_node = ToolNode(tools=tools)
