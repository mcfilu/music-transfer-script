

def get_songs(sp_inst, playlist_url):
    data = []
    result = sp_inst.playlist_tracks(playlist_url)['items']
    for song in result:
        data.append({'song': song['track']['name'], 'artist': song['track']['album']['artists'][0]['name']})
    print(result[0]['track']['album']['artists'][0]['name'])
    print(result[0]['track']['name'])
    print(result[0]['track']['id'])
    return data
