from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from third_party.linkedin import scrape_linkedin_profile

if __name__ == "__main__":
    print("Hello icebreaker")
    summary_template = """
        given the information about a person I want to create:
        1. a short summary
        2. two interesting facts about them
    """

    prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    chain = prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile("https://foo/bar", mock=True)
    res = chain.invoke(input={"information": linkedin_data})
    print(res)
