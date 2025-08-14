from langgraph.graph import END, StateGraph

from graph.const import GENERATE, GRADE_DOCUMENTS, RETRIEVE, WEBSEARCH
from graph.nodes import generate, grade_documents, retrieve, web_search
from graph.state import GraphState


def decide_to_generate(state):
    print("---ASSESS GRADED DOCUMENTS---")
    if state["web_search"]:
        print("---WEB SEARCH---")
        return WEBSEARCH
    else:
        print("---GERERATE---")
        return GENERATE


workflow = StateGraph(GraphState)

workflow.add_node(RETRIEVE, retrieve)
workflow.add_node(GRADE_DOCUMENTS, grade_documents)
workflow.add_node(WEBSEARCH, web_search)
workflow.add_node(GENERATE, generate)

workflow.set_entry_point(RETRIEVE)

workflow.add_edge(RETRIEVE, GRADE_DOCUMENTS)
workflow.add_conditional_edges(
    GRADE_DOCUMENTS, decide_to_generate, {GENERATE: GENERATE, WEBSEARCH: WEBSEARCH}
)
workflow.add_edge(WEBSEARCH, GENERATE)
workflow.add_edge(GENERATE, END)

app = workflow.compile()
app.get_graph().draw_mermaid_png(output_file_path="graph.png")
