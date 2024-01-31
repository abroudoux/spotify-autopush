import os
from typing import Dict, Any
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Spotify:

    def __init__(self) -> None:
        self.spotify_client_id = os.getenv("SPOTIFY_CLIENT_ID")
        self.spotify_client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        self.spotify_redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

    def __get_last_album_played_data(self) -> Dict[str, Any]:
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
        album_cover_url = album_cover_art[0]['url'] if album_cover_art and len(album_cover_art) > 0 else print("No album cover URL found.")
        album_url = recently_saved_album['external_urls']['spotify'] if 'external_urls' in recently_saved_album else print("No album URL found.")

        artist_name = album_artist[0]['name'] if album_artist and len(album_artist) > 0 else print("The property 'name' was not found in the recently played album.")

        album_data: Dict[str, Any] = {"album_name": album_name, "artist_name": artist_name, "album_cover_url": album_cover_url, "album_url": album_url}

        return album_data

    def return_last_album_played(self):
        album_data = self.__get_last_album_played_data()
        artist_name = album_data['artist_name']
        album_name = album_data['album_name']
        last_album_played_cover_url = album_data['album_cover_url']
        last_album_played = f"{artist_name} - {album_name}"

        return last_album_played, last_album_played_cover_url
