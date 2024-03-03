from pytube import YouTube, Search
import os


def get_stream(song, artist):
    query = f"{song} {artist}"
    yt = Search(query).results[0]
    return yt.streams.filter(only_audio=True).first()


def get_streams_list(songs_list):
    streams_list = []
    for song in songs_list:
        streams_list.append(get_stream(song['song'], song['artist']))
    return streams_list


def download_songs(songs_list):
    streams_list = get_streams_list(songs_list)
    cur_dir = os.path.dirname(os.path.abspath(__file__))
    temp_dir = os.path.join(cur_dir, 'temp_songs_folder')
    os.makedirs(temp_dir)
    for stream in streams_list:
        stream.download(output_path=temp_dir)