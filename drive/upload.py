from pydrive.drive import GoogleDrive
from helpers.config import determine_temp_music_path
import os


def upload_file(drive, song_name, folder_id):
    new_song = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": folder_id}],
                                 "title": song_name, "mimeType": "audio/mp4"})
    song_path = os.path.join(determine_temp_music_path(), song_name)
    new_song.SetContentFile(song_path)
    new_song.Upload()


def upload_folder(gauth, folder_name):
    drive = GoogleDrive(gauth)

    # Create folder
    folder_metadata = {'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder'}
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()

    folder_id = folder['id']

    songs_folder_path = determine_temp_music_path()
    print(songs_folder_path)
    songs = os.listdir(songs_folder_path)
    print(songs)
    for song in songs:
        upload_file(drive, song, folder_id)