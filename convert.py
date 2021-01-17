from spotify import get_playlist_tracks
from youtube import call_youtube

def convert(spotify_uri):
  playlist_tuple = get_playlist_tracks(spotify_uri)
  playlist_url = call_youtube(playlist_tuple)
  return playlist_url