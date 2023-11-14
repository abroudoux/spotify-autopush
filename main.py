def get_current_track(access_token):
    reponse = requests.get(SPOTIFY_GET_CURRENT_TRACK_URL, headers={"Authorization": f"Bearer {access_token}"})
