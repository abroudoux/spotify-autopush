from spotify_autopush.src.models.spotify import Spotify
from spotify_autopush.src.models.env_loader import EnvLoader

def app():
    env_loader = EnvLoader()

    if env_loader.check():
        spotify = Spotify()
        album_data = spotify.get_current_album()
        print(album_data)
        # update_readme_template(album_data)
    else:
        print("Checkup failed. Please check your environment variables.")


# def update_readme_template(album_data):

#     with open("profile.md", "r", encoding="utf-8") as file:
#         template_content = file.read()

#     updated_template = template_content.replace("${album_name}", album_data['album_name'])
#     updated_template = updated_template.replace("${album_artist}", album_data['artist_name'])
#     updated_template = updated_template.replace("${album_cover_url}", album_data['album_cover_url'])
#     updated_template = updated_template.replace("${album_url}", album_data['album_url'])

#     print("Contenu du modèle après mise à jour :")
#     print(updated_template)

#     with open("profile.md", "w", encoding="utf-8") as file:
#         file.write(updated_template)

