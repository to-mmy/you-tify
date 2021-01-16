from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class ApiKeys(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    spotifyPlaylistUrl= db.Column(db.String(200), nullable=False)
    youtubeClientId = db.Column(db.String(200), nullable=False)
    youtubeClientSecret = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<ApiKeys(playlistId=%s, spotifyClientId=%s, youtubeApiKey=%s, youtubeClientId=%s)>' % (self.playlistId, self.spotifyClientId, self.youtubeApiKey, self.youtubeClientId)

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == "POST":
        spotify_playlist_url = request.form.get('spotify_playlist_url', False)
        youtube_client_id = request.form.get('youtubeClientId', False)
        youtube_client_secret = request.form.get('youtubeClientSecret', False)

        new_api_keys = ApiKeys(spotifyPlaylistUrl=spotify_playlist_url, youtubeClientId=youtube_client_id, youtubeClientSecret=youtube_client_secret)
        try:
            db.session.add(new_api_keys)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue creating your playlist."
    else:
        return render_template('index.html', error = error)

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