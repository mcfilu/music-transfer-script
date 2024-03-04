# music-transfer-script

## Project Overview
The Music Transfer Script is a Python application designed to transfer music playlists from Spotify to Google Drive. It utilizes the Spotify API to fetch playlist information and the PyDrive library to upload music files to Google Drive. Additionally, it leverages the PyTube library to download songs from YouTube.

## Project Structure
The project structure is organized as follows:

```bash

music-transfer-script/
│
├── spotify/
│   ├── credentials.py
│   └── loader.py
│
├── youtube/
│   └── download.py
│
├── drive/
│   ├── auth.py
│   └── upload.py
│
├── helpers/
│   ├── config.py
│   └── clear.py
├── tests/
│
├── main.py
└── config.json
```
spotify/: Contains modules for handling Spotify API credentials and loading playlist data.

youtube/: Contains a module for downloading songs from YouTube.

drive/: Contains modules for authenticating with Google Drive and uploading music files.

helpers/: Contains utility modules such as config and clear for managing configurations and cleaning up temporary files.

tests/: Contains unit and integration tests for most of the functions within the application.

main.py: Main entry point of the application.

config.json: Configuration file containing Spotify API credentials and Google Drive API key.

## Functionality Requirements
The Music Transfer Script supports the following functionality:

Fetching playlist information from Spotify.
Downloading songs from YouTube.
Uploading downloaded music files to Google Drive.

## Prerequisites
Before running the Music Transfer Script, ensure you have the following prerequisites installed:

Python 3.7
PyTube
PyDrive
Spotipy

## How to Run
Clone the repository:
```bash
git clone https://github.com/mcfilu/music-transfer-script
```
Navigate to the project directory:

```bash
cd music-transfer-script
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

Configure the config.json file with your Spotify API credentials and Google Drive API key.

## Run the script:

```bash
python main.py <playlist_url>
```
Replace <playlist_url> with the URL of the Spotify playlist you want to transfer.