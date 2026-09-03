"""Calculator tool used by the LangGraph agent."""

from simpleeval import simple_eval
from langchain_core.tools import tool


@tool
def calculator(expression: str) -> str:
    """Use this tool for arithmetic calculations.

    Supports +, -, *, /, ** and parentheses.
    """
    try:
        return str(simple_eval(expression))
    except Exception:
        return "Invalid mathematical expression."
