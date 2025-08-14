import os

from graph.graph import app

if __name__ == "__main__":
    os.environ["LANGSMITH_PROJECT"] = "crag-agent"
    print("Hello Advanced RAG")
    print(app.invoke(input={"question": "what is agent memory?"}))
