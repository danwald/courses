from typing import Any

from langchain_tavily import TavilySearch

from graph.state import GraphState
from langchain.schema import Document

web_search_tool = TavilySearch(max_results=3)


def web_search(state: GraphState) -> dict[str, Any]:
    question, documents = state["question"], state["documents"] or []

    tavily_results = web_search_tool.invoke({"query": question})["results"]
    tavily_corpus = "\n".join(result["content"] for result in tavily_results)
    web_docs = Document(page_content=tavily_corpus)
    if web_docs is not None:
        documents.append(web_docs)
    else:
        documents = [web_docs]

    return {"question": question, "documents": documents}


if __name__ == "__main__":
    result = web_search(state={"question": "agent memory", "documents": None})
    print(f"Question: {result['question']} Results:{len(result['documents'])}")
