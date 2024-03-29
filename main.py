from helpers.config import load_credentials
from spotify.credentials import auth_user, create_instance
from spotify.loader import get_songs, get_name
from youtube.download import download_songs
from drive.auth import authenticate
from drive.upload import upload_folder
from helpers.clear import delete_downloads
import sys


def main(playlist_url):
    # playlist_url = "https://open.spotify.com/playlist/2odeDPVVEP0MEvwqpTnMLN"
    spotify_id, spotify_secret, drive_key = load_credentials()
    token = auth_user(client_id=spotify_id, client_secret=spotify_secret)
    spotipy_ins = create_instance(token)
    songs = get_songs(spotipy_ins, playlist_url)
    playlist_name = get_name(spotipy_ins, playlist_url)
    download_songs(songs)
    drive_instance = authenticate()
    upload_folder(drive_instance, playlist_name)
    delete_downloads()


if __name__ == "__main__":
    try:
        parameter = sys.argv[1]
    except Exception:
        raise KeyError("Application requires one argument: playlist url passed as a string")
    main(parameter)
