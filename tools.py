from simpleeval import simple_eval
from langchain_core.tools import tool
from langchain_community.utilities import WikipediaAPIWrapper, GoogleSerperAPIWrapper
from langchain_community.tools import WikipediaQueryRun, GoogleSerperRun


# Wikipedia tool
wiki_api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=300,
)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)


# Google Search tool
google_api_wrapper = GoogleSerperAPIWrapper(k=1)
google_search_tool = GoogleSerperRun(api_wrapper=google_api_wrapper)


# Calculator tool
@tool
def calculator(expression: str) -> str:
    """Use this tool for arithmetic calculations.

    Supports +, -, *, /, ** and parentheses.
    """
    try:
        return str(simple_eval(expression))
    except Exception:
        return "Invalid mathematical expression."


tools = [wiki_tool, google_search_tool, calculator]
