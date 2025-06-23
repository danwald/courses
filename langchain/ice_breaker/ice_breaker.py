from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from third_party.linkedin import scrape_linkedin_profile
from third_party.twitter import get_user_tweets
from agents.linkedin_lookup import lookup
from agents.twitter_handle import lookup as twitter_lookup
from output_parsers import summary_parser, Summary


def ice_break_with(name: str, mock: bool = False) -> tuple[Summary, str]:
    linkedin_url = lookup(name)
    linkedin_data = scrape_linkedin_profile(linkedin_url, mock=mock)

    twitter_handle = twitter_lookup(name)
    tweets = get_user_tweets(twitter_handle, mock=mock)

    summary_template = """
        given the linkedin information {information} about a person and their latest twitter posts {twitter_posts} want to create:
        1. a short summary
        2. two interesting facts about them
        Use information from both linkedin and twitter
        \n{format_instructions}
    """

    prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    chain = prompt_template | llm | summary_parser

    res: Summary = chain.invoke(
        input={"information": linkedin_data, "twitter_posts": tweets}
    )

    return res, linkedin_data.get("photoUrl", "")


if __name__ == "__main__":
    print("icebreaker")
    ice_break_with("danny crasto dubai")
