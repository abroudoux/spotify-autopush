import typer
from spotify_autopush.src.models.spotify import Spotify
from spotify_autopush.src.commands.cmd_checkup import checkup


app = typer.Typer(rich_help_panel="rich")

def app():
    if checkup():
        spotify = Spotify()
        spotify.get_current_album()
