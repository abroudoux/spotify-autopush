from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import requests
import os
import json
from typing import Any, Dict
class Github:
    """
    A class to interact with the Github API for managing user profile information and issues.

    This class encapsulates methods for updating the biography and status of a Github user's profile and for creating issues in a specified repository. It handles authentication and provides a simplified interface for making specific Github API calls.

    Attributes:
    -----------
    username (str): Github username used for authentication.
    base_url (str): Base URL for the Github API.
    base_grapql_url (str): Base URL for the Github GraphQL API.
    auth (HTTPBasicAuth): Authentication object with credentials.

    Methods:
    --------
    update_bio(content): Updates the biography of the Github user's profile.
    update_status(content): Updates the status of the Github user's profile.
    """

    def __init__(self) -> None:
        load_dotenv()

        """
        Initializes the Github object with authentication details.

        Sets up the authentication credentials for accessing the Github API using a personal access token stored in environment variables. Configures the base URLs for standard and GraphQL API endpoints.
        """
        self.username: str = os.getenv("GITHUB_USERNAME")
        self.base_url: str = "https://api.github.com"
        self.base_graphql_url: str = "https://api.github.com/graphql"
        self.auth: HTTPBasicAuth = HTTPBasicAuth(
            self.username, os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
        )
        self.headers = {
            'Authorization': f'bearer {os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")}',
            'Content-Type': 'application/json'
        }

    def update_readme(self, album_response: dict) -> Dict[str, Any]:
        """
        Updates the README of the Github user's profile.

        Sends a PUT request to the Github API to update the README file in the user's profile repository.

        Parameters:
        -----------
        album_response (dict): The album response object from Spotify.

        Returns:
        --------
        Dict[str, Any]: The JSON response from the Github API.

        Raises:
        -------
        requests.HTTPError: If the HTTP request results in an unsuccessful status code.
        """
        headers = {
            'Authorization': f'bearer {os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")}',
            'Content-Type': 'application/json'
        }
        data = {
            'message': 'Update README',
            'content': album_response['content'],
            'sha': album_response['sha']
        }
        response = requests.put(url=f"{self.base_url}/repos/{self.username}/{self.repo}/contents/README.md",
                                auth=self.auth, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        return response.json()
