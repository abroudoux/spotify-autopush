from rich import print
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

        client_id = os.getenv("SPOTIFY_CLIENT_ID")
        client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

        if not client_id:
            print("Please define the environment variable SPOTIPY_CLIENT_ID.")
            return False

        if not client_secret:
            print("Please define the environment variable SPOTIPY_CLIENT_SECRET.")
            return False

        if not redirect_uri:
            print("Please define the environment variable SPOTIPY_REDIRECT_URI.")
            return False

        return True