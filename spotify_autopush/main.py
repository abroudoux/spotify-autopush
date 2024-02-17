from spotify_autopush.src.models.env_loader import EnvLoader
from spotify_autopush.src.models.spotify import Spotify
from spotify_autopush.src.models.github import Github

def app():
    env_loader = EnvLoader()

    if env_loader.check():
        spotify = Spotify()
        github = Github()
        last_album_played_data = spotify.get_last_album_played_data()
        github.udpate_readme(last_album_played_data)
        # github.get_portfolio()
    else:
        print("Checkup failed. Please check your environment variables.")