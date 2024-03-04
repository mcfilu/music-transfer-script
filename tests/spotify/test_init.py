import pytest
from unittest.mock import patch
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import Spotify

from spotify.credentials import auth_user, create_instance


@patch("spotipy.oauth2.SpotifyClientCredentials.get_access_token")
def test_auth_user_success(mock_get_access_token):
    """Tests if auth_user returns a valid token when credentials are provided."""
    mock_get_access_token.return_value = {"access_token": "valid_token"}
    client_id = "your_client_id"
    client_secret = "your_client_secret"

    token = auth_user(client_id, client_secret)

    assert token == "valid_token"


@patch("spotipy.oauth2.SpotifyClientCredentials.get_access_token")
def test_auth_user_missing_credentials(mock_get_access_token):
    """Tests if auth_user raises an error when credentials are not provided."""
    mock_get_access_token.return_value = {"access_token": "valid_token"}

    with pytest.raises(TypeError):
        auth_user()

    with pytest.raises(TypeError):
        auth_user(client_id="your_client_id")


@patch("spotipy.Spotify")
def test_create_instance(mock_spotify):
    """Tests if create_instance returns a Spotify object with a valid token."""
    token = "valid_token"

    sp = create_instance(token)

    assert isinstance(sp, Spotify)
    mock_spotify.assert_called_once_with(auth=token)
