from langchain import hub  # type: ignore
from langchain.agents import (
    create_react_agent,
    AgentExecutor,
)
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from tools.tools import get_profile_url_tavily


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    template = """given the name or person {name_of_person} I want you to find a link to their twitter profile and extract from it their username.
                          Your answer should contain only a username"""
    prompt_template = PromptTemplate(
        template=template, input_variables=["name_of_person"]
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google 4 twitter profile page",
            func=get_profile_url_tavily,
            description="useful for when you need get the twitter Page URL",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linked_profile_url = str(result["output"])
    return linked_profile_url


if __name__ == "__main__":
    print(lookup("danny crasto dubai"))
