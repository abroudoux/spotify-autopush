from dotenv import load_dotenv
import os

class Twitter:
    # def __init__(self):
    #     load_dotenv()

    #     self.api_key: str = os.getenv("TWITTER_API_KEY")
    #     self.api_secret: str = os.getenv("TWITTER_API_SECRET")

    def create_tweet(self, last_album_played_data):
        """
        Create a tweet.

        Args:
        last_album_played_data (dict): The last album played data.

        Returns:
        str: The tweet.
        """
        tweet = f"I'm currently listening to {last_album_played_data['album_name']} by {last_album_played_data['artist_name']}."
        print(tweet)
        return tweet
