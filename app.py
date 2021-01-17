from flask import Flask, render_template, redirect, url_for, request
from convert import convert

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    error = None
    completed = None
    if request.method == "POST":
        spotify_playlist_url = request.form.get('spotifyPlaylistUrl', False)
        try:
            completed = convert(spotify_playlist_url)
            return render_template('index.html', error = error, completed = completed)
        except:
            error = "There was an error creating your playlist."
            return render_template('index.html', error = error, completed = completed)
    else:
        return render_template('index.html', error = error, completed = completed)

if __name__ == "__main__":
    app.run(debug=True)