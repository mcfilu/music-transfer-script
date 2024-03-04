import pytest
from unittest.mock import patch
from spotipy import Spotify
from spotify.loader import get_songs, get_name


@patch("spotipy.Spotify.playlist_tracks")
def test_get_songs_success(mock_playlist_tracks):
    """Tests if get_songs returns a list of songs with details from a playlist."""
    mock_playlist_tracks.return_value = {
        "items": [
            {
                "track": {
                    "name": "Song 1",
                    "album": {"artists": [{"name": "Artist 1"}]},
                }
            },
            {
                "track": {
                    "name": "Song 2",
                    "album": {"artists": [{"name": "Artist 2"}]},
                }
            },
        ]
    }
    playlist_url = "https://open.spotify.com/playlist/..."
    sp_inst = Spotify("fake_token")  # Mock Spotify instance

    songs = get_songs(sp_inst, playlist_url)

    assert len(songs) == 2  # Check length of returned list
    assert songs[0] == {"song": "Song 1", "artist": "Artist 1"}  # Check song details
    assert songs[1] == {"song": "Song 2", "artist": "Artist 2"}


@patch("spotipy.Spotify.playlist_tracks")
def test_get_songs_empty_playlist(mock_playlist_tracks):
    """Tests if get_songs returns an empty list for an empty playlist."""
    mock_playlist_tracks.return_value = {"items": []}
    playlist_url = "https://open.spotify.com/playlist/..."
    sp_inst = Spotify("fake_token")

    songs = get_songs(sp_inst, playlist_url)

    assert songs == []


@patch("spotipy.Spotify.playlist")
def test_get_name_success(mock_playlist):
    """Tests if get_name returns the playlist name from the provided URL."""
    mock_playlist.return_value = {"name": "My Playlist"}
    playlist_url = "https://open.spotify.com/playlist/..."
    sp_inst = Spotify("fake_token")

    name = get_name(sp_inst, playlist_url)

    assert name == "My Playlist"


@patch("spotipy.Spotify.playlist")
def test_get_name_invalid_url(mock_playlist):
    """Tests if get_name returns None for an invalid playlist URL."""
    mock_playlist.side_effect = spotipy.exceptions.SpotifyException("Invalid playlist URL")
    playlist_url = "invalid_url"
    sp_inst = Spotify("fake_token")

    name = get_name(sp_inst, playlist_url)

    assert name is None


# Remember to replace "fake_token" with your actual Spotify access token before running tests.
