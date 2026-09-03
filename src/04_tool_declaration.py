from langchain_community.utilities import WikipediaAPIWrapper, GoogleSerperAPIWrapper
from langchain_community.tools import WikipediaQueryRun, GoogleSerperRun


wiki_api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=300,
)
wiki_tool = WikipediaQueryRun(api_wrapper=wiki_api_wrapper)


google_api_wrapper = GoogleSerperAPIWrapper(k=1)
google_search_tool = GoogleSerperRun(api_wrapper=google_api_wrapper)
