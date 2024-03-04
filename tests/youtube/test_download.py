import os
import pytest
from unittest.mock import patch
from unittest import mock
from pytube import YouTube, Search
from youtube.download import get_stream, get_streams_list, download_songs


@patch("pytube.Search")
def test_get_stream_success(mock_search):
    """Tests if get_stream returns the first audio stream for a search."""
    mock_search.return_value = Search(query="Song Artist")
    mock_result = mock_search.return_value.results[0]
    mock_stream = mock.Mock()
    mock_stream.filter.return_value = [mock.Mock()]
    mock_stream.filter.return_value[0] = mock_stream  # First element is the audio stream
    mock_result.streams = mock_stream

    stream = get_stream("Song", "Artist")

    assert stream is mock_stream


@patch("pytube.Search")
def test_get_stream_no_audio_stream(mock_search):
    """Tests if get_stream returns None when no audio stream is found."""
    mock_search.return_value = Search(query="Song Artist")
    mock_result = mock_search.return_value.results[0]
    mock_stream = mock.Mock()
    mock_stream.filter.return_value = []  # No audio streams
    mock_result.streams = mock_stream

    stream = get_stream("Song", "Artist")

    assert stream is None


def test_get_streams_list_success():
    """Tests if get_streams_list returns a list of streams from a song list."""
    songs_list = [{"song": "Song 1", "artist": "Artist 1"}, {"song": "Song 2", "artist": "Artist 2"}]

    # Mock stream objects (replace with actual mocking for pytube)
    stream1 = mock.Mock()
    stream2 = mock.Mock()

    # Simulate getting streams (replace with actual mocking for pytube)
    with patch("your_script.get_stream", side_effect=[stream1, stream2]):
        streams_list = get_streams_list(songs_list)

    assert len(streams_list) == 2
    assert streams_list[0] is stream1
    assert streams_list[1] is stream2


@patch("os.makedirs")
@patch("pytube.YouTube.download")
def test_download_songs_success(mock_download, mock_makedirs):
    """Tests if download_songs downloads songs from a stream list."""
    songs_list = [{"song": "Song 1", "artist": "Artist 1"}, {"song": "Song 2", "artist": "Artist 2"}]

    # Mock stream objects (replace with actual mocking for pytube)
    stream1 = mock.Mock()
    stream2 = mock.Mock()

    # Simulate getting streams (replace with actual mocking for pytube)
    with patch("your_script.get_stream", side_effect=[stream1, stream2]):
        download_songs(songs_list)

    mock_makedirs.assert_called_once_with(os.path.join(os.getcwd(), "temp_songs_folder"))
    mock_download.assert_called_twice()  # Each stream downloads once
