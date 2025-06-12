from typing import Any

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from third_party.linkedin import scrape_linkedin_profile
from third_party.twitter import get_user_tweets
from agents.linkedin_lookup import lookup
from agents.twitter_handle import lookup as twitter_lookup


def ice_breakwith(name: str, mock: bool = False) -> Any:
    linkedin_url = lookup(name)
    linkedin_data = scrape_linkedin_profile(linkedin_url, mock=mock)

    twitter_handle = twitter_lookup(name)
    tweets = get_user_tweets(twitter_handle, mock=mock)

    return linkedin_data, tweets


if __name__ == "__main__":
    print("icebreaker")
    summary_template = """
        given the linkedin information {information} about a person and their latest twitter posts {twitter_posts} want to create:
        1. a short summary
        2. two interesting facts about them
        Use information from both linkedin and twitter
    """

    prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    chain = prompt_template | llm | StrOutputParser()

    linkedin_data, tweets = ice_breakwith("danny crasto dubai", mock=True)
    res = chain.invoke(input={"information": linkedin_data, "twitter_posts": tweets})
    print(res)
