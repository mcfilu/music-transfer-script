import json
import os


def determine_config_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, '..', 'config.json')
    return config_path


def determine_temp_music_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    music_path = os.path.join(script_dir, '..', 'youtube', 'temp_songs_folder')
    return music_path


def check_file():
    config_path = determine_config_path()
    result = os.path.isfile(config_path)
    if not result:
        raise FileNotFoundError("Program needs config.json file in a root directory")
    return result


def load_credentials():
    config_path = determine_config_path()
    if check_file():
        with open(config_path, 'r') as cred_file:
            credentials = json.load(cred_file)
            if not 'spotify_id' in credentials:
                raise KeyError("spotify_id key has to be in the config.json file")
            if not 'spotify_secret' in credentials:
                raise KeyError("spotify_secret key has to be in the config.json file")
            if not 'drive_key' in credentials:
                raise KeyError("google_api key has to be in the config.json file")
            return credentials['spotify_id'], credentials['spotify_secret'], credentials['drive_key']

load_credentials()