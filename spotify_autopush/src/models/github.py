import base64
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
        filepath = os.path.join(os.getcwd(), "spotify_autopush", "profile_readme.md")
        with open(filepath, "w") as f:
            f.write(self.readme_content)

    def udpate_readme(self, last_played_album, album_cover_url):
        self.__get_readme()
        new_content = f'<p>{last_played_album}</p>\n'
        self.readme_content = self.readme_content.replace('<p>', new_content)
        print(album_cover_url)
        self.__save_readme()
        r = requests.put(
            f'{self.base_url}/repos/{self.username}/{self.repo}/contents/profile_readme.md',
            json={
                "message": "Update README with last played album",
                "content": base64.b64encode(self.readme_content.encode()).decode(),
            },
            headers=self.headers,
        )
        print("Status:", r.status_code)
