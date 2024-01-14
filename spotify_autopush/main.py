import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
from spotify_autopush.src.models.spotify import Spotify

def app():
    load_dotenv()

    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

    if not client_id:
        print("Please define the environment variable SPOTIPY_CLIENT_ID.")
        return

    if not client_secret:
        print("Please define the environment variable SPOTIPY_CLIENT_SECRET.")

    if not redirect_uri:
        print("Please define the environment variable SPOTIPY_REDIRECT_URI.")

    spotify = Spotify()

    spotify.get_current_album()

