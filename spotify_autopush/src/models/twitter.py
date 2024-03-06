from dotenv import load_dotenv
import os
import requests
import tweepy
from requests_oauthlib import OAuth1Session
import json

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
        self.api_key_secret: str = os.getenv("TWITTER_API_KEY_SECRET")
        self.bearer_token: str = os.getenv("TWITTER_BEARER_TOKEN")
        self.client_id: str = os.getenv("TWITTER_CLIENT_ID")
        self.client_secret: str = os.getenv("TWITTER_CLIENT_SECRET")
        self.acces_token: str = os.getenv("TWITTER_ACCESS_TOKEN")
        self.access_token_secret: str = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        self.consumer_key = self.api_key
        self.consumer_secret = self.api_key_secret
        self.request_token_url: str = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
        self.oauth = OAuth1Session(self.consumer_key, client_secret=self.consumer_secret)

    def test_github(self, last_album_played_data: dict):
        tweet_text = f'{last_album_played_data['album_name']} - {last_album_played_data['artist_name']}'
        # tweet_image = f'{last_album_played_data['album_cover_url']}'
        payload = {"text": tweet_text}

        try:
            fetch_response = self.oauth.fetch_request_token(self.request_token_url)
        except ValueError:
            print(
                "There may have been an issue with the consumer_key or consumer_secret you entered."
            )

        resource_owner_key = fetch_response.get("oauth_token")
        resource_owner_secret = fetch_response.get("oauth_token_secret")
        print("Got OAuth token: %s" % resource_owner_key)

        base_authorization_url = "https://api.twitter.com/oauth/authorize"
        authorization_url = self.oauth.authorization_url(base_authorization_url)
        print("Please go here and authorize: %s" % authorization_url)
        verifier = input("Paste the PIN here: ")

        access_token_url = "https://api.twitter.com/oauth/access_token"
        oauth = OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=resource_owner_key,
            resource_owner_secret=resource_owner_secret,
            verifier=verifier,
        )
        oauth_tokens = oauth.fetch_access_token(access_token_url)

        access_token = oauth_tokens["oauth_token"]
        access_token_secret = oauth_tokens["oauth_token_secret"]

        oauth = OAuth1Session(
            self.consumer_key,
            client_secret=self.consumer_secret,
            resource_owner_key=access_token,
            resource_owner_secret=access_token_secret,
        )

        response = oauth.post(
            "https://api.twitter.com/2/tweets",
            json=payload,
        )

        if response.status_code != 201:
            raise Exception(
                "Request returned an error: {} {}".format(response.status_code, response.text)
            )

        print("Response code: {}".format(response.status_code))

        json_response = response.json()
        print(json.dumps(json_response, indent=4, sort_keys=True))



