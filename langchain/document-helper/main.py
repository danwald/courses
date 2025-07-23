import os

import streamlit as st
from backend.core import run_llm

USER_PROMPT_KEY = "uph"
CHAT_ANS_KEY = "cah"
CHAT_KEY = "ch"

st.set_page_config(
    page_title="Your App Title",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

for k in (USER_PROMPT_KEY, CHAT_KEY, CHAT_ANS_KEY):
    if k not in st.session_state:
        st.session_state[k] = []


def create_sources_string(source_urls: list[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(set(source_urls))
    sources_list.sort()
    sources_string = "sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i + 1}. {source}\n"
    return sources_string


prompt = st.text_input("prompt", placeholder="How can I help you?")

if prompt:
    with st.spinner("Generating input .."):
        gen_result = run_llm(prompt)
        sources = [
            str(doc.metadata["source"]) for doc in gen_result["source_documents"]
        ]
        formatted_response = (
            f"{gen_result['result']} \n\n {create_sources_string(sources)}"
        )

        st.session_state[USER_PROMPT_KEY].append(prompt)
        st.session_state[CHAT_ANS_KEY].append(formatted_response)
        st.session_state[CHAT_KEY].append(("human", prompt))
        st.session_state[CHAT_KEY].append(("ai", gen_result["result"]))

if st.session_state[CHAT_ANS_KEY]:
    for query, res in zip(
        st.session_state[USER_PROMPT_KEY], st.session_state[CHAT_ANS_KEY]
    ):
        st.chat_message("user").write(query)
        st.chat_message("assistant").write(res)
