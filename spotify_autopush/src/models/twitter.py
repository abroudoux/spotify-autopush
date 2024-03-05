from dotenv import load_dotenv
import os
import requests
import tweepy

class Twitter:
    def __init__(self):
        """
        Class constructor.

        Attributes:
        api_key (str): The Twitter API key.
        api_secret (str): The Twitter API secret.
        base_url (str): The Twitter API base URL.
        """

        load_dotenv()

        self.api_key: str = os.getenv("TWITTER_API_KEY")
        self.api_secret: str = os.getenv("TWITTER_API_KEY_SECRET")
        self.bearer_token: str = os.getenv("TWITTER_BEARER_TOKEN")
        self.client_id: str = os.getenv("TWITTER_CLIENT_ID")
        self.client_secret: str = os.getenv("TWITTER_CLIENT_SECRET")

        client = tweepy.Client(bearer_token=self.bearer_token)

        query = "covid -is:retweet"

        response = client.search_recent_tweets(query=query, max_results=10)

        return response

    def test(self, response):
        print(response)


