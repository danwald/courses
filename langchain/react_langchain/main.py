def get_text_length(text: str) -> int:
    """Returns  the length of text by characters"""
    return len(text)


if __name__ == "__main__":
    txt = "Hello React Langchain"
    print(f"'{txt}' is {get_text_length(txt)} characters long")
