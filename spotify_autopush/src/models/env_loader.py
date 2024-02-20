import os
from dotenv import load_dotenv

class EnvLoader:
    """
    A class used to check if the environment variables are set correctly.

    This class encapsulates methods for checking if the environment variables are set correctly. It handles authentication and provides a simplified interface for making specific Github API calls.

    Attributes:
    -----------

    Methods:
    --------
    checkup(): Prints the current environment variable values set in the .env file.
    """

    def check(self):
        """
        Checks if the environment variables are set correctly.
        """
        return self.__run_checkup()

    def __run_checkup(self):
        """
        Prints the current environment variable values set in the .env file.
        Check if the environment variables are set correctly.
        """
        load_dotenv()

        spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
        spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        spotify_redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")
        github_username = os.getenv("GITHUB_USERNAME")
        github_personal_access_token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
        # twitter_api_key = os.getenv("TWITTER_API_KEY")
        # twitter_api_secret = os.getenv("TWITTER_API_SECRET")
        # twitter_beaaer_token = os.getenv("TWITTER_BEARER_TOKEN")

        if not spotify_client_id:
            print("Please define the environment variable SPOTIPY_CLIENT_ID.")
            return False

        if not spotify_client_secret:
            print("Please define the environment variable SPOTIPY_CLIENT_SECRET.")
            return False

        if not spotify_redirect_uri:
            print("Please define the environment variable SPOTIPY_REDIRECT_URI.")
            return False

        if not github_username:
            print("Please define the environment variable GITHUB_USERNAME.")
            return False

        if not github_personal_access_token:
            print("Please define the environment variable GITHUB_PERSONAL_ACCESS_TOKEN.")
            return False

        # if not twitter_api_key:
        #     print("Please define the environment variable TWITTER_API_KEY.")
        #     return False

        # if not twitter_api_secret:
        #     print("Please define the environment variable TWITTER_API_SECRET.")
        #     return False

        # if not twitter_beaaer_token:
        #     print("Please define the environment variable TWITTER_BEARER_TOKEN.")
        #     return False

        return True