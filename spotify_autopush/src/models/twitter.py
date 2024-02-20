# from dotenv import load_dotenv
# import os
# import requests
# from requests_oauthlib import OAuth1

# class Twitter:
#     def __init__(self):
#         """
#         Class constructor.

#         Attributes:
#         api_key (str): The Twitter API key.
#         api_secret (str): The Twitter API secret.
#         base_url (str): The Twitter API base URL.
#         auth (OAuth1): The Twitter API OAuth1 authentication.
#         """

#         load_dotenv()

#         self.api_key: str = os.getenv("TWITTER_API_KEY")
#         self.api_secret: str = os.getenv("TWITTER_API_SECRET")
#         self.base_url: str = "https://api.twitter.com/2/tweets"
#         self.auth = OAuth1(self.api_key, self.api_secret)

#     def create_tweet(self, last_album_played_data):
#         """
#         Create a tweet.

#         Args:
#         last_album_played_data (dict): The last album played data.

#         Returns:
#         str: The tweet.
#         """
#         tweet = f"I'm currently listening to {last_album_played_data['album_name']} by {last_album_played_data['artist_name']}."
#         return tweet

#     def post_tweet(self, tweet):
#         """
#         Post a tweet.

#         Args:
#         tweet (str): The tweet.
#         """

#         r = requests.post(
#             f'{self.base_url}', 
#             json={"text": tweet},
#             auth=self.auth,
#         )
#         print("Status:", r.status_code, r.reason)

