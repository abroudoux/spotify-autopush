from spotify_autopush.src.models.env_loader import EnvLoader
from spotify_autopush.src.models.spotify import Spotify
from spotify_autopush.src.models.github import Github
from spotify_autopush.main import app

def test_app(monkeypatch, capsys):
    monkeypatch.setattr(EnvLoader, "check", lambda self: True)

    class MockSpotify:
        def get_last_album_played_data(self):
            return "Last album played data"

    class MockGithub:
        def udpate_readme(self, data):
            print(f"Updating readme with data: {data}")

    monkeypatch.setattr(Spotify, "__init__", lambda self: None)
    monkeypatch.setattr(Github, "__init__", lambda self: None)
    monkeypatch.setattr(Spotify, "get_last_album_played_data", MockSpotify.get_last_album_played_data)
    monkeypatch.setattr(Github, "udpate_readme", MockGithub.udpate_readme)

    app()

    captured = capsys.readouterr()

    assert captured.out == "Updating readme with data: Last album played data\n"
