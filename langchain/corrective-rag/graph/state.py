from typing import TypedDict


class GraphState(TypedDict):
    question: str
    generation: str
    web_search: str
    documents: list[str]
