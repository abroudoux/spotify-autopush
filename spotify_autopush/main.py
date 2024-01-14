import spotipy
import os
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

def app():
    load_dotenv()

    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

    if not client_id:
        print("Veuillez définir la variable d'environnement SPOTIPY_CLIENT_ID.")
        return

    if not client_secret:
        print("Veuillez définir la variable d'environnement SPOTIPY_CLIENT_SECRET.")

    if not redirect_uri:
        print("Veuillez définir la variable d'environnement SPOTIPY_REDIRECT_URI.")

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope="user-library-read"))

    results = sp.current_user_saved_tracks()
    for idx, item in enumerate(results['items']):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])

