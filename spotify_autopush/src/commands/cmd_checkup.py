import typer
from rich import print
from pathlib import Path
import os
from dotenv import load_dotenv


app = typer.Typer(rich_help_panel="rich")

@app.command(rich_help_panel="Utils & Configs")
def checkup():
    """
    Prints the current environment variable values set in the .env file.
    Check if the environment variables are set correctly.
    """
    load_dotenv()

    client_id = os.getenv("SPOTIFY_CLIENT_ID")
    client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
    redirect_uri = os.getenv("SPOTIFY_REDIRECT_URI")

    if not client_id:
        print("Please define the environment variable SPOTIPY_CLIENT_ID.")
        return False

    if not client_secret:
        print("Please define the environment variable SPOTIPY_CLIENT_SECRET.")
        return False

    if not redirect_uri:
        print("Please define the environment variable SPOTIPY_REDIRECT_URI.")
        return False

    return True
