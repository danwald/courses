from typing import Any

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from third_party.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup import lookup


def ice_breakwith(name: str, mock: bool = False) -> Any:
    url = lookup(name)
    linkedin_data = scrape_linkedin_profile(url, mock=mock)
    return linkedin_data


if __name__ == "__main__":
    print("icebreaker")
    summary_template = """
        given the information {information} about a person I want to create:
        1. a short summary
        2. two interesting facts about them
    """

    prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    chain = prompt_template | llm | StrOutputParser()
    linkedin_data = ice_breakwith("danny crasto dubai", mock=True)
    res = chain.invoke(input={"information": linkedin_data})
    print(res)
