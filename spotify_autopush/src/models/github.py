import base64
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import requests
import os

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
        """
        Initializes the Github object with authentication details.

        Sets up the authentication credentials for accessing the Github API using a personal access token stored in environment variables. Configures the base URLs for standard and GraphQL API endpoints.
        """
        load_dotenv()
        self.username: str = os.getenv("GITHUB_USERNAME")
        self.repo: str = self.username
        self.base_url: str = "https://api.github.com"
        self.base_graphql_url: str = "https://api.github.com/graphql"
        self.auth: HTTPBasicAuth = HTTPBasicAuth(
            self.username, os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
        )
        self.headers = {
            'Authorization': f'bearer {os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")}',
            'Content-Type': 'application/json'
        }
        self.api_token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")

    def __get_bio(self,context):
        """
        Gets the biography of the Github user's profile.

        Sends a GET request to the Github API to retrieve the biography of the user's profile.

        Parameters:
        -----------
        context (str): The context to print before the biography.

        Raises:
        -------
        requests.HTTPError: If the HTTP request results in an unsuccessful status code.
        """
        r = requests.get('https://api.github.com/user', headers=self.headers)
        json_data = r.json()
        print(context + json_data["bio"])

    def update_bio(self, new_bio: str):
        """
        Updates the biography of the Github user's profile.

        Sends a PATCH request to the Github API to update the biography of the user's profile.

        Raises:
        -------
        requests.HTTPError: If the HTTP request results in an unsuccessful status code.
        """
        self.__get_bio("Old bio: ")
        bio_patch = requests.patch('https://api.github.com/user', json = {'bio': "Last album played : " + new_bio}, headers=self.headers)
        print ("Status:", bio_patch.status_code)
        self.get_bio("New bio: ")

    def __get_readme(self):
        """
        Gets the README of the Github user's profile.

        Sends a GET request to the Github API to retrieve the README of the user's profile.

        Raises:
        -------
        requests.HTTPError: If the HTTP request results in an unsuccessful status code.
        """
        r = requests.get(f'{self.base_url}/repos/{self.username}/{self.repo}/readme', headers=self.headers)
        json_data = r.json()
        self.readme_content = base64.b64decode(json_data["content"]).decode('utf-8')
        self.__save_readme()

    def __save_readme(self):
        """
        Saves the README of the Github user's profile to a file.

        Raises:
        -------
        requests.HTTPError: If the HTTP request results in an unsuccessful status code.
        """
        filepath = os.path.join(os.getcwd(), "spotify_autopush", "profile_readme.md")
        with open(filepath, "w") as f:
            f.write(self.readme_content)

    def udpate_readme(self, last_played_album):
        """
        Updates the README of the Github user's profile with the last played album.

        Sends a PUT request to the Github API to update the README of the user's profile with the last played album.

        Parameters:
        -----------
        last_played_album (str): The last played album.

        Raises:
        -------
        requests.HTTPError: If the HTTP request results in an unsuccessful status code.
        """
        self.__get_readme()
        new_content = f'<p style="color: #CCCCCC;">{last_played_album}</p>\n'
        self.readme_content = self.readme_content.replace('<p>', new_content)
        self.__save_readme()
        r = requests.put(f'{self.base_url}/repos/{self.username}/{self.repo}/contents/profile_readme.md',
                        json={"message": "Update README with last played album", "content": base64.b64encode(self.readme_content.encode()).decode()},
                        headers=self.headers)
        print("Status:", r.status_code)