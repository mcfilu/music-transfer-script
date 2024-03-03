import json
import os

def check_file():
    result = os.path.isfile('../config.json')
    if not result:
        raise FileNotFoundError("Program needs config.json file in a root directory")
    return result

def load_credentials():
    if check_file():
        with open('../config.json', 'r') as cred_file:
            credentials = json.load(cred_file)
            if not 'spotify_id' in credentials:
                raise KeyError("spotify_id key has to be in the config.json file")
            if not 'spotify_secret' in credentials:
                raise KeyError("spotify_secret key has to be in the config.json file")
            if not 'drive_key' in credentials:
                raise KeyError("google_api key has to be in the config.json file")
            return credentials
