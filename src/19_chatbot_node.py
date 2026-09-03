from importlib import import_module

State = import_module("src.12_state").State
llm_with_tools = import_module("src.17_bind_tools").llm_with_tools


def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}
