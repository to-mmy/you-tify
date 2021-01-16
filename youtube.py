import os
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Limitations: User must create a channel. This can be accomplished by making a public playlist.

# This function takes in an input of the spotify playlist and performs the YouTube playlist creation and song population api calls
# The output of this function is a URL of the newly created YouTube playlist

# For example:
# playlist = [{"song_name": "Can I Call You Tonight", "artists": "Dayglow"}]
# playlist_name = "Example Playlist"
# client_id = "540128384418-crf1ir3g8dr6ocq4do19f6j6c4ekgdb2.apps.googleusercontent.com"
# client_secret = "izXecB2_zIPOJWi_kErlUiNx"

def call_youtube(client_id, client_secret, playlist):

    # Turn the inputs into a clients_secret_file
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

    # client_secrets_file = json.dumps(client_id_and_secrets)

    scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

    # Create a flow object. Note: this takes in input as a string?
    flow = InstalledAppFlow.from_client_config(client_secrets_file, scopes)

    # After running the code, the user will be prompted to give authorization to the application
    credentials = flow.run_local_server(port=8080, prompt="consent")

    youtube = build("youtube", "v3", credentials=credentials)

    """request = youtube.playlists().list(
        part="snippet,contentDetails",
        channelId=None,
        maxResults=25,
        mine=True
    )

    response = request.execute()

    print(response)
    print(response["pageInfo"]["totalResults"])"""

    # Create a private playlist through an API call
    create_playlist = youtube.playlists().insert(
            part="snippet,status",
            body={
                "snippet": {
                "title": playlist_name,
                "defaultLanguage": "en"
                },
                "status": {
                "privacyStatus": "private"
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

    playlist_url = "https://www.youtube.com/playlist?list={playlist_id}"

    return playlist_url
