from pydrive.drive import GoogleDrive
import os


def upload_file(drive, song):
    file1 = drive.CreateFile({'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
    file1.SetContentString('Hello World!') # Set content of the file from given string.
    file1.Upload()


def upload_folder(gauth, folder_name):
    drive = GoogleDrive(gauth)

    # Create folder
    folder_metadata = {'title': folder_name, 'mimeType': 'application/vnd.google-apps.folder'}
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()

    # Upload file to folder
    folder_id = folder['id']
    file = drive.CreateFile({"parents": [{"kind": "drive#fileLink", "id": folder_id}]})
    file.SetContentFile('testfile.txt')
    file.Upload()

    # songs = os.listdir()
    # for song in songs:
    #     upload_file(drive, song)