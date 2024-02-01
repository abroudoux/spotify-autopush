import base64
import re
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
import requests
import os

class Github:

    def __init__(self) -> None:
        load_dotenv()
        self.username: str = os.getenv("GITHUB_USERNAME")
        self.repo: str = self.username
        self.base_url: str = "https://api.github.com"
        self.base_graphql_url: str = "https://api.github.com/graphql"
        self.auth: HTTPBasicAuth = HTTPBasicAuth(self.username, os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN"))
        self.headers = {'Authorization': f'bearer {os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")}', 'Content-Type': 'application/json'}
        self.api_token = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")

    def __get_bio(self,context):
        r = requests.get('https://api.github.com/user', headers=self.headers)
        json_data = r.json()
        print(context + json_data["bio"])

    def update_bio(self, new_bio: str):
        self.__get_bio("Old bio: ")
        bio_patch = requests.patch('https://api.github.com/user', json = {'bio': "Last album played : " + new_bio}, headers=self.headers)
        print ("Status:", bio_patch.status_code)
        self.get_bio("New bio: ")

    def __get_readme(self):
        r = requests.get(f'{self.base_url}/repos/{self.username}/{self.repo}/readme', headers=self.headers)
        json_data = r.json()
        self.readme_content = base64.b64decode(json_data["content"]).decode('utf-8')
        self.__save_readme()

    def __save_readme(self):
        filepath = os.path.join(os.getcwd(), "spotify_autopush", "README.md")
        with open(filepath, "w") as f:
            f.write(self.readme_content)

    def udpate_readme(self, last_played_album, album_cover_url):
        self.__get_readme()

        new_last_album_played = f'<p>{last_played_album}</p>'
        self.readme_content = re.sub(r'<p>.*?</p>', new_last_album_played, self.readme_content, flags=re.DOTALL)

        new_last_album_played_cover_url = f'<img style="width: 250px;" src="{album_cover_url}"/>'
        self.readme_content = re.sub(r'<img[^>]*>', new_last_album_played_cover_url, self.readme_content)

        self.__save_readme()

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
