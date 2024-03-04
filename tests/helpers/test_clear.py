import os
import pytest
from helpers.clear import delete_downloads


def test_delete_downloads():
    """Tests if the function deletes files and the folder."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    temp_folder = os.path.join(script_dir, '..', '..', 'youtube', 'temp_songs_folder')
    os.makedirs(temp_folder, exist_ok=True)
    file1 = os.path.join(temp_folder, "file1.txt")
    file2 = os.path.join(temp_folder, "file2.mp3")
    with open(file1, "w") as f:
        f.write("test")
    with open(file2, "w") as f:
        f.write("test")

    delete_downloads()

    assert not os.path.exists(temp_folder)  # Checks if folder is deleted
    assert not os.path.exists(file1)  # Checks if files are deleted
    assert not os.path.exists(file2) # Checks if second file is deleted


def test_delete_missing_folder():
    with pytest.raises(FileNotFoundError):
        delete_downloads()
