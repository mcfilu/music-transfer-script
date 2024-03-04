import os
import shutil
import tempfile
import pytest
from helpers.clear import delete_downloads


@pytest.fixture
def temp_folder():
    curr_path = os.path.dirname(os.path.abspath(__file__))
    temp_dir = tempfile.mkdtemp(os.path.join(curr_path, '..', '..', 'youtube', 'temp_songs_folder'))
    yield temp_dir
    shutil.rmtree(temp_dir)


def test_delete_downloads(temp_folder):
    # Create some dummy files
    files = ['file1.txt', 'file2.txt', 'file3.txt']
    for file in files:
        open(os.path.join(temp_folder, file), 'w').close()
    # Call the function
    delete_downloads()
    # Assert that the folder is empty
    assert len(os.listdir(temp_folder)) == 0
    assert not os.path.exists(temp_folder)


def test_delete_downloads_no_files(temp_folder):
    # Call the function without creating any files
    delete_downloads()
    # Assert that the folder is empty
    assert len(os.listdir(temp_folder)) == 0
    assert not os.path.exists(temp_folder)

