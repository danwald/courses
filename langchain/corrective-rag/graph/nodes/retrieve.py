from typing import Any

from ingestion import retriever

from graph.state import GraphState


def retrieve(state: GraphState) -> dict[str, Any]:
    question = state["question"]
    docs = retriever.invoke({"question": question})
    return {"documents": docs, "question": question}
