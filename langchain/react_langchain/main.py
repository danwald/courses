from langchain_core.prompts import PromptTemplate
from langchain_core.tools.render import render_text_description
from langchain_core.agents import AgentAction, AgentFinish
from langchain_openai import ChatOpenAI
from langchain.agents.output_parsers.react_single_input import ReActSingleInputOutputParser
from langchain.agents import tool


@tool  # type: ignore
def get_text_length(text: str) -> int:
    """Returns  the length of text by characters"""
    return len(text.strip("\n").strip('"').strip("'"))

def find_tool_by_name(name: str, tools: [str]) -> str:
    for tll in tools:
        if tll.name == name:
            return tll
    raise ValueError(f'Tool:{name} not found')

if __name__ == "__main__":
    txt = "Hello React Langchain"
    result = get_text_length.invoke({"text": txt})
    tools = [get_text_length]
    template = """
    Answer the following questions as best you can. You have access to the following tools:

    {tools}

    Use the following format:

    Question: the input question you must answer
    Thought: you should always think about what to do
    Action: the action to take, should be one of [{tool_names}]
    Action Input: the input to the action
    Observation: the result of the action
    ... (this Thought/Action/Action Input/Observation can repeat N times)
    Thought: I now know the final answer
    Final Answer: the final answer to the original input question

    Begin!

    Question: {input}
    Thought:
    """
    prompt = PromptTemplate(template=template).partial(
        tools=render_text_description(tools), tool_names=",".join(t.name for t in tools)
    )
    llm = ChatOpenAI(temperature=0, stop=["\nObservation", "Observation"])
    agent = {"input": lambda x: x['input']} | prompt | llm | ReActSingleInputOutputParser()
    agent_step: [AgentAction | AgentFinish] = agent.invoke({"input": "What's the length of the word 'DOG'?"})
    if isinstance(agent_step, AgentAction):
        tool_name = agent_step.tool
        tooled = find_tool_by_name(tool_name, tools)
        tool_input = agent_step.tool_input
        obs = tooled.func(tool_input)
        print(obs)
