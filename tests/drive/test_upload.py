import pytest
from unittest.mock import patch, Mock
from pydrive.drive import GoogleDrive
from drive.upload import upload_file, upload_folder


@patch("pydrive.drive.GoogleDrive")
def test_upload_file_success(mock_drive):
    """Tests successful upload of a single file."""
    song_name = "test_song.mp3"
    folder_id = "123456"

    mocked_drive = Mock(GoogleDrive)
    mock_drive.CreateFile.return_value = Mock(
        SetContentFile=Mock(),
        Upload=Mock()
    )
    mock_drive.__enter__.return_value = mocked_drive

    # Patch determine_temp_music_path (optional)
    with patch("helpers.config.determine_temp_music_path") as mock_path:
        mock_path.return_value = "/path/to/temp/music"

    upload_file(mocked_drive, song_name, folder_id)

    # Verify calls and arguments
    mock_drive.CreateFile.assert_called_once_with({
        "parents": [{"kind": "drive#fileLink", "id": folder_id}],
        "title": song_name,
        "mimeType": "audio/mp4"
    })
    mocked_drive.SetContentFile.assert_called_once_with("/path/to/temp/music/test_song.mp3")
    mocked_drive.Upload.assert_called_once_with()


@patch("pydrive.drive.GoogleDrive")
def test_upload_folder_success(mock_drive):
    """Tests successful upload of a folder and its contents."""
    folder_name = "test_folder"
    gauth = Mock()  # Mock the authentication object

    mocked_drive = Mock(GoogleDrive)
    mock_drive.CreateFile.return_value = Mock(
        Upload=Mock()  # Only mock methods used in the function
    )
    mock_drive.__enter__.return_value = mocked_drive

    # Patch determine_temp_music_path (optional)
    with patch("helpers.config.determine_temp_music_path") as mock_path:
        mock_path.return_value = "/path/to/temp/music"

    # Mock songs in the folder
    songs = ["song1.mp3", "song2.mp4"]
    os.listdir.return_value = songs

    upload_folder(gauth, folder_name)

    # Verify calls and arguments (partially)
    mock_drive.CreateFile.assert_called_once_with({
        "title": folder_name,
        "mimeType": "application/vnd.google-apps.folder"
    })
    mocked_drive.Upload.assert_called_once_with()

    # Verify upload_file calls within the function (loop through mocked songs)
    for i, song in enumerate(songs):
        upload_file_args = (mocked_drive, song, folder_name)
        assert upload_file.call_count == i + 1  # Check calls incrementally
        upload_file.assert_called_with(*upload_file_args)


# @patch("pydrive.drive.GoogleDrive")
# def test_upload_file_error(mock_drive):
#     """Tests upload_file behavior with an error during upload."""
#     song_name = "error_song.mp3"
#     folder_id = "123456"
#
#     mocked_drive = Mock(GoogleDrive)
#     mock_drive.CreateFile.return_value = Mock(Upload=Mock(side_effect=Exception("Upload error")))
#     mock_drive.__enter__.return_value = mocked_drive
#
#     with pytest.raises(Exception) as excinfo:
#         upload_file(mocked_drive, song_name, folder_id)
#
#     assert "Upload error"
