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

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope="user-read-recently-played"))

    results = sp.current_user_recently_played(limit=1)

    if results and 'items' in results and len(results['items']) > 0:
        most_recent_track = results['items'][0]['track']

        if 'name' in most_recent_track:
            track_name = most_recent_track['name']
            print(f"Nom du morceau le plus récent : {track_name}")
        else:
            print("La propriété 'name' n'est pas présente dans les données du morceau.")
    else:
        print("Aucun morceau récemment joué trouvé.")

