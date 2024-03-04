import pytest
from unittest.mock import patch, MagicMock
from unittest import mock
from main import main
from helpers.config import load_credentials
from drive.upload import upload_folder
from helpers.clear import delete_downloads


@patch("spotify.credentials.auth_user", return_value="fake_token")
@patch("spotify.loader.get_songs", return_value=["song1", "song2"])
@patch("spotify.loader.get_name", return_value="My Playlist")
@patch("youtube.download.download_songs", return_value=None)  # No return value needed
@patch("drive.auth.authenticate", return_value="drive_instance")
def test_main_success(mock_auth, mock_download, mock_get_name, mock_get_songs, mock_auth_user):
    """Tests main function flow with successful execution."""
    # Mock load_credentials to return dummy values
    load_credentials.return_value = "id", "secret", "key"

    main("https://example.com/playlist")

    # Verify calls and arguments (partially)
    load_credentials.assert_called_once_with()
    mock_auth_user.assert_called_once_with(client_id="id", client_secret="secret")
    mock_get_songs.assert_called_once_with(mock.sentinel.spotipy_instance, "https://example.com/playlist")
    mock_get_name.assert_called_once_with(mock.sentinel.spotipy_instance, "https://example.com/playlist")
    mock_download.assert_called_once_with(["song1", "song2"])
    upload_folder.assert_called_once_with("drive_instance", "My Playlist")
    delete_downloads.assert_called_once_with()


def test_main_raises_error_for_missing_argument():
    """Tests main function behavior when an argument is missing."""
    with pytest.raises(TypeError) as excinfo:
        main()

    assert "main() missing 1 required positional argument: 'playlist_url'" in str(excinfo.value)
