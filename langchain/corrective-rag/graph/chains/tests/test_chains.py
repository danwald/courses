import pytest
from ingestion import retriever

from graph.chains.generation import generation_chain
from graph.chains.retrieval_grader import GradeDocuments, retrieval_grader


@pytest.mark.parametrize(
    ("question", "expected"),
    (
        ("agent memory", "yes"),
        ("how can I make chicago deepdish pizza", "no"),
    ),
)
def test_retrival_grader(question: str, expected: str) -> None:
    question = question
    docs = retriever.invoke(question)
    doc_txt = docs[1].page_content

    res: GradeDocuments = retrieval_grader.invoke(
        {
            "document": doc_txt,
            "question": question,
        }
    )
    assert res.binary_score == expected


def test_generation_chain() -> None:
    question = "agent_memory"
    docs = retriever.invoke(question)
    gen = generation_chain.invoke({"context": docs, "question": question})
    print(gen)
