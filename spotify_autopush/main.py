from spotify_autopush.src.models.spotify import Spotify
from spotify_autopush.src.models.env_loader import EnvLoader

def app():
    env_loader = EnvLoader()

    if env_loader.check():
        spotify = Spotify()
        album_data = spotify.get_current_album()
        print(album_data)
    else:
        print("Checkup failed. Please check your environment variables.")