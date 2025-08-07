from typing import Any

from graph.state import GraphState
from ingestion import retriever


def retrieve(state: GraphState) -> dict[str, Any]:
    question = state["question"]
    docs = retriever.invoke({"question": question})
    return {"documents": docs, "question": question}
