from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class ApiKeys(object):
    def __init__(self, spotifyPlaylistUrl):
        self.spotifyPlaylistUrl = spotifyPlaylistUrl

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    completed = None
    if request.method == "POST":
        spotify_playlist_url = request.form.get('spotify_playlist_url', False)
        new_api_keys = ApiKeys(spotifyPlaylistUrl=spotify_playlist_url)
        try:
            completed = "https://www.youtube.com/watch?v=dQw4w9WgXcQ" # backend_function(new_api_keys)
            return render_template('index.html', error = error, completed = completed)
        except:
            error = "There was an issue creating your playlist."
            return render_template('index.html', error = error, completed = completed)
    else:
        return render_template('index.html', error = error, completed = completed)

# @app.route('/new', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == "POST":
#         spotify_playlist_id = request.form['spotifyPlaylistId']
#         spotify_client_id = request.form['spotifyClientId']
#         spotify_client_secret = request.form['spotifyClientSecret']
#         youtube_api_key = request.form['youtubeApiKey']
#         youtube_client_id = request.form['youtubeClientId']
#         youtube_client_secret = request.form['youtubeClientSecret']

#         new_api_keys = ApiKeys(spotifyPlaylistId=spotify_playlist_id, spotifyClientId=spotify_client_id, spotifyClientSecret=spotify_client_secret, youtubeApiKey=youtube_api_key, youtubeClientId=youtube_client_id, youtubeClientSecret=youtube_client_secret)
#         try:
#             db.session.add(new_api_keys)
#             db.session.commit()
#             return redirect('/')
#         except:
#             return "There was an issue creating your playlist."
#     else:
#         return render_template('new.html', error = error)

if __name__ == "__main__":
    app.run(debug=True)