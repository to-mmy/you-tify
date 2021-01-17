import spotipy
import re
from spotipy.oauth2 import SpotifyClientCredentials
import os

def get_playlist_tracks(playlist_url):
    # Pass client id and client secret into SpotifyClientCredentials() and authenticate request
    SPOTIPY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
    SPOTIPY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
    auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
    sp = spotipy.Spotify(auth_manager = auth_manager)

    # extract playlist id from playlist url
    m = re.search('playlist/(.+?)\?', playlist_url)
    playlist_id = ""
    if(m):
        playlist_id = m.group(1)
    else: #id must be at the end of the url
        for c in reversed(playlist_url):
            if c == '/':
                break
            playlist_id += c
        playlist_id = playlist_id[::-1]

    # playlist name and items
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