import os
import json
import tempfile
import pytest
import shutil
from helpers.config import (
    determine_config_path,
    determine_temp_music_path,
    check_file,
    load_credentials,
)



@pytest.fixture
def temp_folder():
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    shutil.rmtree(temp_dir)


@pytest.fixture
def temp_config(temp_folder):
    config_path = os.path.join(temp_folder, 'config.json')
    with open(config_path,
        "r") as f:
        json.dump({"spotify_id": "your_spotify_id", "spotify_secret": "your_spotify_secret", "drive_key": "your_drive_key"}, f)
        yield config_path


def test_determine_config_path():
    config_path = determine_config_path()
    assert os.path.isfile(config_path)


def test_determine_temp_music_path():
    temp_music_path = determine_temp_music_path()
    assert os.path.isdir(temp_music_path)


def test_check_file_exists(temp_config):
    assert check_file()


def test_check_file_does_not_exist(temp_folder):
    with pytest.raises(FileNotFoundError):
        check_file()


def test_load_credentials(temp_config):
    spotify_id, spotify_secret, drive_key = load_credentials()
    assert spotify_id == "your_spotify_id"
    assert spotify_secret == "your_spotify_secret"
    assert drive_key == "your_drive_key"


def test_load_credentials_missing_keys(temp_folder):
    config_path = os.path.join(temp_folder, 'config.json')
    with open(config_path, "w") as f:
        json.dump({"invalid_key": "value"}, f)
    with pytest.raises(KeyError):
        load_credentials()


def test_load_credentials_missing_file(temp_folder):
    with pytest.raises(FileNotFoundError):
        load_credentials()

