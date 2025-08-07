from typing import Any, Dict

from graph.chains.retrieval_grader import GradeDocuments, retrieval_grader
from graph.state import GraphState


def grade_documents(state: GraphState) -> Dict[str, Any]:
    """
    Determines whether the retrieved documents are relevant to the question
    If any document is not relevant, we will set a flag to run web search

    Args:
        state (dict): The current graph state

    Returns:
        state (dict): Filtered out irrelevant documents and updated web_search state
    """

    question, docs, filtered_docs, web_search = (
        state["question"],
        state["documents"],
        [],
        False,
    )

    for doc in docs:
        res: GradeDocuments = retrieval_grader.invoke(
            {"question": question, "document": doc.page_content}
        )

        if res.binary_score == "yes":
            filtered_docs.append(doc)
        else:
            web_search = True
    return {"question": question, "document": filtered_docs, "web_search": web_search}
