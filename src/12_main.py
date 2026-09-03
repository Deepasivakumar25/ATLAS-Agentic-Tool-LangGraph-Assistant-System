from importlib import import_module

from langchain_core.messages import HumanMessage


graph = import_module("src.11_graph_compile").graph

THREAD_CONFIG = {"configurable": {"thread_id": "conversation_1"}}


def chat():
    print("ATLAS - Agentic Tool & LangGraph Assistant System")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() in {"exit", "quit", "q"}:
            print("Goodbye!")
            break

        if not user_input:
            continue

        result = graph.invoke(
            {"messages": [HumanMessage(content=user_input)]},
            config=THREAD_CONFIG,
        )

        print("ATLAS:", result["messages"][-1].content)
        print()


if __name__ == "__main__":
    chat()
