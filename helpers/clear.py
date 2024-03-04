from helpers.config import determine_temp_music_path
import os
import shutil


def delete_downloads():
    folder_path = determine_temp_music_path()
    try:
        folder = os.listdir(folder_path)
    except Exception:
        raise FileNotFoundError("The clearing delete_downloads function couldnt find the temp music folder")
    for file in folder:
        os.remove(os.path.join(folder_path, file))
    shutil.rmtree(folder_path)
