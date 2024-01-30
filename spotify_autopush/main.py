from spotify_autopush.src.models.spotify import Spotify
from spotify_autopush.src.models.env_loader import EnvLoader

from spotify_autopush.src.models.github import Github

def app():
    env_loader = EnvLoader()

    if env_loader.check():
        spotify = Spotify()
        last_played_album = spotify.print_last_played_album()

        github = Github()
        # github.update_bio(last_played_album)
        github.udpate_readme(last_played_album)
    else:
        print("Checkup failed. Please check your environment variables.")