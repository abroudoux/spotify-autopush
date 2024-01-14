import os
import requests
from typing import Dict, Any
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spotify:
    """
    A class for fetching and formatting music information from the Spotify API.

    This class provides functionality to retrieve current album playing and format it for display or further use.

    Attributes:
    -----------

    Methods:
    --------
    """

    def __init__(self) -> None:
        """
        Initializes the Spotify instance.
        """

        self.spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
        self.spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        self.spotify_redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

    def get_current_album(self) -> Dict[str, Any]:
        """
        Fetches the currently playing album from the Spotify API.

        This method uses the Spotify API to fetch the currently playing album. It returns the album's name, artist, and cover art URL in a dictionary.

        Returns:
        --------
        Dict[str, Any]: A dictionary containing the album's name, artist, and cover art URL.
        """
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.spotify_client_id, client_secret=self.spotify_client_secret, redirect_uri=self.spotify_redirect_uri, scope="user-library-read"))

        results = sp.current_user_saved_albums(limit=1)

        if results and 'items' in results and len(results['items']) > 0:
            recently_saved_album = results['items'][0]['album']

            if 'name' in recently_saved_album:
                album_name = recently_saved_album['name']
                print(f"Nom du dernier album sauvegardé : {album_name}")
            else:
                print("La propriété 'name' n'est pas présente dans les données de l'album.")
        else:
            print("Aucun album récemment joué trouvé.")

        return {
            "name": "test",
            "artist": "test",
            "cover_art_url": "test"
        }
