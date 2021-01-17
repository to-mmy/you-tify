from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.errors

# Limitations: User must create a channel. This can be accomplished by making a public playlist.

# This function takes in an input of the spotify playlist and performs the YouTube playlist creation and song population api calls
# The output of this function is a URL of the newly created YouTube playlist

# For example:
# playlist_tuple = ({'name': 'SB Hacks Test Playlist'}, [{'song_name': 'Away from Home', 'artists': 'Jhove Bert'}, {'song_name': 'Cereal Killa', 'artists': 'Blue Wednesday'}])


def call_youtube(playlist_tuple):
    
    playlist_name = playlist_tuple[0]["name"]
    playlist = playlist_tuple[1]
    
    # Start the authentication with the app
    client_id = "540128384418-crf1ir3g8dr6ocq4do19f6j6c4ekgdb2.apps.googleusercontent.com"
    client_secret = "izXecB2_zIPOJWi_kErlUiNx"
    
    # Turn the inputs into a clients_secret_file dictionary to obtain credentials
    client_secrets_file = {
        "web":{ 
            "client_id":client_id,
            "project_id":"sbhacksvii-you-tify",
            "auth_uri":"https://accounts.google.com/o/oauth2/auth",
            "token_uri":"https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
            "client_secret":client_secret
            }
        }
    
    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
    
    # Create a flow object
    flow = InstalledAppFlow.from_client_config(client_secrets_file, scopes)
    
    # After running the code, the user will be prompted to give authorization to the application
    credentials = flow.run_local_server(port=8080)
    
    youtube = build("youtube", "v3", credentials=credentials)

    # Create a private playlist through an API call
    create_playlist = youtube.playlists().insert(
            part="snippet,status",
            body={
                "snippet": {
                "title": playlist_name,
                "defaultLanguage": "en"
                },
                "status": {
                "privacyStatus": "unlisted"
                }
            }
        )
    
    new_playlist = create_playlist.execute()
    
    playlist_id = new_playlist["id"]
    
    for song in playlist:
        
        song_name = song["song_name"]
        artist = song["artists"]
        
        # Key words for the search
        keywords = song_name + " " + artist + " audio"
        
        searched_list = youtube.search().list(
                part="snippet",
                maxResults=1,
                q=keywords
            )
        searched_song = searched_list.execute()
        
        searched_id = searched_song["items"][0]["id"]["videoId"]
        
        add_playlist_item = youtube.playlistItems().insert(
                part="snippet",
                body={
                    "snippet": {
                        "playlistId" : playlist_id,
                        "resourceId": {
                            "kind": "youtube#video",
                            "videoId": searched_id
                        }
                    }
                }
            )
        
        new_playlist_item = add_playlist_item.execute()
    
    playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"
    
    return playlist_url

# url = call_youtube(playlist_tuple)
