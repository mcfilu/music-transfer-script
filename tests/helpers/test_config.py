import os
import pytest
import json
from helpers.config import (
    determine_config_path,
    determine_temp_music_path,
    check_file,
    load_credentials,
)


def test_determine_config_path():
    expected_path = os.path.join(os.path.dirname(__file__), "..", "..", "config.json")
    assert os.path.samefile(determine_config_path(), expected_path)


def test_determine_temp_music_path():
    expected_path = os.path.join(os.path.dirname(__file__), "..", "..", "youtube", "temp_songs_folder")
    assert os.path.samefile(determine_temp_music_path(), expected_path)


def test_check_file_present():
    config_path = determine_config_path()
    with open(config_path, "w") as f:
        f.write("{}")
    assert check_file() is True


def test_check_file_missing():
    with pytest.raises(FileNotFoundError):
        check_file()


def test_load_credentials_success():
    config_path = determine_config_path()
    with open(config_path, "w") as f:
        json.dump({"spotify_id": "id", "spotify_secret": "secret", "drive_key": "key"}, f)
    spotify_id, spotify_secret, drive_key = load_credentials()
    assert spotify_id == "id"
    assert spotify_secret == "secret"
    assert drive_key == "key"


def test_load_credentials_missing_keys():
    config_path = determine_config_path()
    with open(config_path, "w") as f:
        json.dump({"spotify_id": "id"}, f)
    with pytest.raises(KeyError):
        load_credentials()

