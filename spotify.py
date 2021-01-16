import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
from pprint import pprint

# Pass client_id and client_secret into SpotifyClientCredentials() and authenticate request
SPOTIPY_CLIENT_ID='86a8193d3384455f877df20a02c35057'
SPOTIPY_CLIENT_SECRET='0da856aab0aa4c56ab46ceee51153560'
auth_manager = SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager = auth_manager)

# prompt user for the playlist id (Spotify URI)
playlist_id = input("Spotify URI: ") # 'spotify:playlist:4ap5vo2narR8BB9LZc6nfq'
# print(playlist_id)
offset = 0

# prints playlist name, description, and spotify URI
print(sp.playlist(playlist_id, fields='name, description, uri'))

# prints details of all the tracks in the playlist: track title, artist name(s), album name (and total # of tracks)
while True:
    response = sp.playlist_items(playlist_id,
        offset=offset,
        fields='items(track(name, artists(name), album(name))), total', #, artists(name), album(name)
        additional_types=['track'])
    
    if len(response['items']) == 0:
        break
    
    pprint(response['items'])
    offset += len(response['items'])
    print(offset, "/", response['total'])


# def get_playlist_tracks(username,playlist_id):
#   results = sp.user_playlist_tracks(username,playlist_id)
#   tracks = results['items']
#    while results['next']:
#        results = sp.next(results)
#        tracks.extend(results['items'])
#   return tracks