import base64
import re
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import requests
import os

class Github:
    """
    This class is responsible for interacting with the GitHub API.

    Attributes:
    username (str): The GitHub username.
    repo (str): The GitHub repository name.
    base_url (str): The GitHub API base URL.
    base_graphql_url (str): The GitHub GraphQL API base URL.
    auth (HTTPBasicAuth): The GitHub HTTPBasicAuth object.
    headers (dict): The GitHub API headers.
    api_token (str): The GitHub API token.

    Methods:
    __init__(): The class constructor
    __get_bio(): Get the GitHub user bio.
    update_bio(): Update the GitHub user bio.
    __get_readme(): Get the GitHub repository README.
    __save_readme(): Save the GitHub repository README.
    __commit_readme_github(): Commit the GitHub repository README.
    udpate_readme(): Update the GitHub repository README.
    """

    def __init__(self) -> None:
        """
        Class constructor.

        Attributes:
        username (str): The GitHub username.
        repo (str): The GitHub repository name.
        base_url (str): The GitHub API base URL.
        headers (dict): The GitHub API headers.
        """

        load_dotenv()

        self.username: str = os.getenv("GITHUB_USERNAME")
        self.repo: str = self.username
        self.api_token: str = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
        self.base_url: str = "https://api.github.com"
        self.headers = {'Authorization': f'bearer {self.api_token}', 'Content-Type': 'application/json'}

    def __get_bio(self,context):
        """
        Get the GitHub user bio.

        Parameters:
        context (str): The context to be printed before the bio.

        Returns:
        str: The GitHub user bio.
        """

        r = requests.get('https://api.github.com/user', headers=self.headers)
        json_data = r.json()
        print(context + json_data["bio"])

        return(context + json_data["bio"])

    def update_bio(self, new_bio: str):
        """
        Update the GitHub user bio.

        Parameters:
        new_bio (str): The new bio to be set.
        """

        self.__get_bio("Old bio: ")

        bio_patch = requests.patch('https://api.github.com/user', json = {'bio': "Last album played : " + new_bio}, headers=self.headers)
        print ("Status:", bio_patch.status_code)

        self.__get_bio("New bio: ")

    def __get_readme(self):
        """
        Get the GitHub repository README.

        Returns:
        str: The GitHub repository README.
        """

        r = requests.get(f'{self.base_url}/repos/{self.username}/{self.repo}/readme', headers=self.headers)
        json_data = r.json()
        self.readme_content = base64.b64decode(json_data["content"]).decode('utf-8')

        self.__save_readme()

    def __save_readme(self):
        """
        Save the GitHub repository README.
        """

        filepath = os.path.join(os.getcwd(), "spotify_autopush", "README.md")
        with open(filepath, "w") as f:
            f.write(self.readme_content)

    def __commit_readme_github(self):
        """
        Commit the GitHub repository README.
        """
        response = requests.get(f'{self.base_url}/repos/{self.username}/{self.repo}/contents/README.md', headers=self.headers)
        sha = response.json().get('sha', None)

        r = requests.put(
            f'{self.base_url}/repos/{self.username}/{self.repo}/contents/README.md',
            json={
                "message": "Update README",
                "content": base64.b64encode(self.readme_content.encode()).decode(),
                "sha": sha
            },
            headers=self.headers,
        )
        print("Status:", r.status_code)

    def udpate_readme(self, last_played_album, album_cover_url):
        """
        Update the GitHub repository README.
        Push the changes to the GitHub repository.

        Parameters:
        last_played_album (str): The last played album.
        album_cover_url (str): The album cover URL.
        """

        self.__get_readme()

        new_last_album_played = f'<p>{last_played_album}</p>'
        self.readme_content = re.sub(r'<p>.*?</p>', new_last_album_played, self.readme_content, flags=re.DOTALL)

        new_last_album_played_cover_url = f'<img style="width: 250px;" src="{album_cover_url}"/>'
        self.readme_content = re.sub(r'<img[^>]*>', new_last_album_played_cover_url, self.readme_content)

        self.__save_readme()
        self.__commit_readme_github()
