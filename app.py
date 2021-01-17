from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)