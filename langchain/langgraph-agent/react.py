from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_tavily import TavilySearch


@tool  # type: ignore
def triple(num: float) -> float:
    """
    param num: a number to triple
    returns: the triple of the input number
    """
    return float(num) * 3


tools = [TavilySearch(max_results=1), triple]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0).bind_tools(tools)
