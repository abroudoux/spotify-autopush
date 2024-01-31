from spotify_autopush.src.models.env_loader import EnvLoader
from spotify_autopush.src.models.spotify import Spotify
from spotify_autopush.src.models.github import Github

def app():
    env_loader = EnvLoader()

    if env_loader.check():
        spotify = Spotify()
        github = Github()
        last_album_played, last_album_played_cover_url = spotify.return_last_album_played()
        github.udpate_readme(last_album_played, last_album_played_cover_url)
    else:
        print("Checkup failed. Please check your environment variables.")