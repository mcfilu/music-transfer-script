from spotipy.oauth2 import SpotifyClientCredentials
import spotipy


def auth_user(client_id, client_secret):
    credentials = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    token = credentials.get_access_token()
    return token['access_token']


def create_instance(token):
    sp = spotipy.Spotify(auth=token)
    return sp
