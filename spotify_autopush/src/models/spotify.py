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
    spotify_client_id: str : The Spotify client ID.
    spotify_client_secret: str : The Spotify client secret.
    spotify_redirect_uri: str : The Spotify redirect URI.

    Methods:
    --------
    get_current_album() -> Dict[str, Any]: Fetches the currently playing album from the Spotify API.
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

        if results and 'items' not in results and len(results['items']) == 0:
            print("Any recently played albums were not found.")

        recently_saved_album = results['items'][0]['album']

        if 'name' not in recently_saved_album:
            print("The property 'name' was not found in the recently played album.")

        album_name = recently_saved_album['name']
        album_artist = recently_saved_album['artists']
        album_cover_art = recently_saved_album['images']
        album_cover_url = album_cover_art[0]['url'] if album_cover_art and len(album_cover_art) > 0 else None

        if not album_cover_url:
            print("No album cover URL found.")

        artist_name = album_artist[0]['name'] if album_artist and len(album_artist) > 0 else None

        if  not artist_name:
            print("The property 'name' was not found in the recently played album.")

        album_response: Dict[str, Any] = {
            "album_name": album_name,
            "artist_name": artist_name,
            "album_cover_url": album_cover_url
        }

        return album_response
