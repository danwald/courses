import os
from typing import List, Sequence
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, MessageGraph

from chains import generate_chain, reflect_chain

if __name__ == "__main__":
    print('hello reflexion agent')
    os.environ["LANGSMITH_PROJECT"] = "reflexion-agent"
    response = graph.invoke(inputs)
