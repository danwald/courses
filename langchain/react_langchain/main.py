from langchain.agents import tool


@tool  # type: ignore
def get_text_length(text: str) -> int:
    """Returns  the length of text by characters"""
    return len(text.strip("\n").strip('"'))


if __name__ == "__main__":
    txt = "Hello React Langchain"
    result = get_text_length.invoke({"text": txt})
    tools = [get_text_length]
    print(f"'{txt}' is {result} characters long")
