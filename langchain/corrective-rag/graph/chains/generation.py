from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from langchain import hub

llm = ChatOpenAI(temperature=0)
prompt = hub.pull("rlm/rag-prompt")

generation_chain = prompt | llm | StrOutputParser()
