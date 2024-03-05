import base64
import re
from dotenv import load_dotenv
import requests
import os

class Github:
    """
    This class is responsible for interacting with the GitHub API.

    Attributes:
    username (str): The GitHub username.
    repo (str): The GitHub repository name.
    base_url (str): The GitHub API base URL.
    headers (dict): The GitHub API headers.
    api_token (str): The GitHub API token.

    Methods:
    __init__(): The class constructor
    __get_readme(): Get the GitHub repository README.
    __save_readme(): Save the GitHub repository README.
    __push_readme_github(): Commit the GitHub repository README.
    udpate_readme(): Update the GitHub repository README.
    """

    def __init__(self):
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

        filepath = os.path.join(os.getcwd(), "spotify_autopush", "last_readme.md")
        with open(filepath, "w") as f:
            f.write(self.readme_content)

    def __push_readme_github(self):
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
        print("Status:", r.status_code, r.reason)

    def udpate_readme(self, last_album_played_data):
        """
        Update the GitHub repository README.

        Args:
        last_album_played_data (dict): The last album played data.
        """

        self.__get_readme()

        last_album_played_title = f'{last_album_played_data['album_name']} - {last_album_played_data['artist_name']}'
        last_album_played_cover_url = f'{last_album_played_data['album_cover_url']}'

        new_last_album_played = f'<p>{last_album_played_title}</p>'
        self.readme_content = re.sub(r'<p>.*?</p>', new_last_album_played, self.readme_content, flags=re.DOTALL)

        new_last_album_played_cover_url = f'<img style="width: 250px;" src="{last_album_played_cover_url}"/>'
        self.readme_content = re.sub(r'<img[^>]*>', new_last_album_played_cover_url, self.readme_content)
        self.__save_readme()
        self.__push_readme_github()
