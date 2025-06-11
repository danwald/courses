import os
import requests  # type: ignore
import tweepy


def get_user_tweets(handle: str, num_tweets: int = 5, mock: bool = False) -> list[str]:
    """get twitt handerl,
    Manually scrape the information from the LinkedIn profile"""

    tweets = []
    if mock:
        gist_url = "https://gist.githubusercontent.com/emarco177/9d4fdd52dc432c72937c6e383dd1c7cc/raw/1675c4b1595ec0ddd8208544a4f915769465ed6a/eden-marco-tweets.json"
        tweets = requests.get(
            gist_url,
            timeout=10,
        ).json()

    else:
        client = tweepy.Client(bearer_token=os.environ["TWITTER_BEARER_TOKEN"])
        client = tweepy.Client(
            bearer_token=os.environ["TWITTER_BEARER_TOKEN"],
            consumer_key=os.environ["TWITTER_CONSUMER_KEY"],
            consumer_secret=os.environ["TWITTER_CONSUMER_SECRET"],
            access_token=os.environ["TWITTER_ACCESS_TOKEN"],
            access_token_secret=os.environ["TWITTER_ACCESS_TOKEN_SECRET"],
        )
        uid = client.get_user(username=handle).data.id
        # print(f"{handle} => {uid}")
        tweets = client.get_users_tweets(
            id=uid, max_results=num_tweets, exclude=["retweets", "replies"]
        )

    return [str(t["text"]) for t in tweets[:num_tweets]]


if __name__ == "__main__":
    print(
        get_user_tweets("danwald", mock=False),
    )
