from .config import determine_temp_music_path
import os, shutil


def delete_downloads():
    folder_path = determine_temp_music_path()
    folder = os.listdir(folder_path)
    for file in folder:
        os.remove(os.path.join(folder_path, file))
    shutil.rmtree(folder_path)
