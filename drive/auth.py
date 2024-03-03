from pydrive.auth import GoogleAuth


def authenticate():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return gauth


