from spotify_autopush.src.models.spotify import Spotify
from spotify_autopush.src.models.env_loader import EnvLoader

import json
import requests
from getpass import getpass


api_token = getpass('API Token: ')
h = {'Accept': 'application/vnd.github.v3+json', 'Authorization': 'token ' + api_token}

def app():
    # env_loader = EnvLoader()

    # if env_loader.check():
    #     spotify = Spotify()
    #     album_data = spotify.get_current_album()
    #     print(album_data)
    # else:
    #     print("Checkup failed. Please check your environment variables.")
    get_bio("Old bio: ")
    new_bio = input("Enter new bio: ")
    bio_patch = requests.patch('https://api.github.com/user', json = {'bio': new_bio}, headers = h)
    print ("Status: ", bio_patch.status_code)
    get_bio("New bio: ")


def get_bio(context):
    r = requests.get('https://api.github.com/user', headers=h)
    json_data = r.json()
    print(context + json_data["bio"])