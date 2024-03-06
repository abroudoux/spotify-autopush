from dotenv import load_dotenv
import os
import requests
import tweepy
from requests_oauthlib import OAuth1Session
import json
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
        self.api_key_secret: str = os.getenv("TWITTER_API_KEY_SECRET")
        self.bearer_token: str = os.getenv("TWITTER_BEARER_TOKEN")
        self.client_id: str = os.getenv("TWITTER_CLIENT_ID")
        self.client_secret: str = os.getenv("TWITTER_CLIENT_SECRET")
        self.access_token: str = os.getenv("TWITTER_ACCESS_TOKEN")
        self.access_token_secret: str = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        self.consumer_key = self.api_key
        self.consumer_secret = self.api_key_secret
        self.request_token_url: str = "https://api.twitter.com/oauth/request_token?oauth_callback=oob&x_auth_access_type=write"
        self.oauth = OAuth1Session(self.consumer_key, client_secret=self.consumer_secret)

    def test_github(self, last_album_played_data: dict):
        tweet_text = f'Last album played : {last_album_played_data['album_name']} - {last_album_played_data['artist_name']}'
        album_cover_url = f'{last_album_played_data['album_cover_url']}'
        res = requests.get(album_cover_url)

        path = os.path.join(os.getcwd(), "spotify_autopush", "res", "cover.png")

        with open(path,'wb') as f:
            f.write(res.content)

        auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)

        api = tweepy.API(auth)

        media = api.media_upload(path)
        media_id = media.media_id

        payload = {"text": tweet_text}
        # payload = {"status": tweet_text, "media_ids": [media_id]}

        try:
            fetch_response = self.oauth.fetch_request_token(self.request_token_url)
        except ValueError:
            print(
                "There may have been an issue with the consumer_key or consumer_secret you entered."
            )

        resource_owner_key = fetch_response.get("oauth_token")
        resource_owner_secret = fetch_response.get("oauth_token_secret")

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
            raise requests.exceptions.HTTPError(
                "Request returned an error: {} {}".format(response.status_code, response.text)
            )

        print(payload)
        print("Twitter Status:", response.status_code, response.reason)



