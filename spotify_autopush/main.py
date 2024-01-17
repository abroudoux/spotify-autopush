# import pync
# import os

from spotify_autopush.src.models.spotify import Spotify
from spotify_autopush.src.models.env_loader import EnvLoader

def app():
    env_loader = EnvLoader()

    # script_directory = os.path.dirname(os.path.abspath(__file__))
    # icon_path = os.path.join(script_directory, "assets", "spotify.png")

    if env_loader.check():
        spotify = Spotify()
        album_data = spotify.get_current_album()
        print(album_data)
        update_readme_template(album_data)
    else:
        print("Checkup failed. Please check your environment variables.")


def update_readme_template(album_data):
    template = """
        # Hi there 👋 I'm Arthur, web developer

        📍 I'm based in Angers and Le Mans, France

        🚀 I'm currently working on [Spotify-autopsuh](https://github.com/abroudoux/spotify-autopush.git)

        📚 I'm currently learning Rust, Docker & Python

        🌍 Discover my [Portfolio](https://abroudoux-portfolio.vercel.app/)


        ## Technos & Tools

        [![My Skills](https://skillicons.dev/icons?i=js,typescript,scss,react,tailwind,nestjs,git,bash,nodejs,mongodb,rust,python,postman,docker,postgres,vercel&perline=8)](https://skillicons.dev)

        ## Last played album
        <a href=${album_url} style="text-decoration: none; color: #CCCCCC">
            <div style="border: 1px solid grey; border-radius: 10px; padding: 5px 10px; width: 50%">
                <p style="margin-bottom: 0; font-size: 24px; font-weight: 600">${album_artist} - ${album_name}<p>
                <br>
                <img src=${album_cover_url} style="border-radius: 6px; width: 100%; height: auto">
            </div>
        </a>

        <br>
    """

    updated_template = template.replace("${album_url}", album_data["album_url"])
    updated_template = updated_template.replace("${album_artist}", album_data["artist_name"])
    updated_template = updated_template.replace("${album_name}", album_data["album_name"])
    updated_template = updated_template.replace("${album_cover_url}", album_data["album_cover_url"])

    print(updated_template)
    return updated_template

