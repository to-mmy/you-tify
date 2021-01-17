import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_playlist_tracks(playlist_id):
    # Pass client id and client secret into SpotifyClientCredentials() and authenticate request
    SPOTIPY_CLIENT_ID='e5aa68bb17bd4db1835c3d2faca0aeb1'
    SPOTIPY_CLIENT_SECRET='d6dd8dedd5be4d4cb9338f46d6bef70e'
    auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
    sp = spotipy.Spotify(auth_manager = auth_manager)

    # playlist name
    name = sp.playlist(playlist_id, fields='name')
    response = sp.playlist_items(playlist_id,
            offset=0,
            fields='items(track(name, artists(name))), total',
            additional_types=['track'])

    # list of playlist tracks
    playlist = []
    for i in response['items']:
        artists = []
        for a in i['track']['artists']:
            artists.append(a['name'])
        playlist.append({'song_name':i['track']['name'], 'artists': ' '.join(artists)})
    return(name, playlist)