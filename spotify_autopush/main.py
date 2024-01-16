import pync
import os


from spotify_autopush.src.models.spotify import Spotify
from spotify_autopush.src.models.env_loader import EnvLoader

def app():
    env_loader = EnvLoader()

    script_directory = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(script_directory, "assets", "spotify.png")

    print(icon_path)

    if env_loader.check():
        spotify = Spotify()
        album_data = spotify.get_current_album()
        print(album_data)
        pync.notify(
            "Titre de la notification",
            title="Contenu de la notification",
            appIcon=icon_path,
        )
    else:
        print("Checkup failed. Please check your environment variables.")
