# Introducing, You-tify!

This was a submission for the SB Hacks VII Hackathon. [Our Devpost can be found here.](https://devpost.com/software/you-tify)

You-tify converts your Spotify playlist into a YouTube playlist!

---
## Table of Contents
1. [What it does](#whatitdoes)
2. [Before you use this...](#before)
3. [How do I use You-tify?](#howto)
   * [Prerequisites](#prerequisites)
   * [Directions](#directions)
   * [...Why do I have to follow these directions?](#why)
---

## What it does <a name="whatitdoes"></a>

You-tify takes in a public Spotify Playlist link and, after giving the program access to your account, creates a playlist of the same songs. When you launch the local Web App, you'll be able to paste the Spotify playlist link and then, when you click the URL the application gives, you'll be taken to your transferred playlist.

## Before you use this... <a name="before"></a>

* Please follow the directions below, else this will not work!
* There is a limit to how many songs you can transfer in a day, else there will be an error.
  * This is approximately 60 songs.

## How do I use You-tify? <a name="howto"></a>

Please thoroughly read through this section.

# Prerequisites <a name="prerequisites"></a>

* Python on your computer
* A code editor that supports Python (We used Visual Studio Code)
* (Recommended) Basic knowledge of:
  * Git (to fork, or obtain a copy of this code)
  * pip (installing packages for Python)
  * Using the terminal
  * Creating a virtual environment

# Directions <a name="directions"></a>

1. [Follow this link to obtain your Google client_id and client_secret](https://developers.google.com/adwords/api/docs/guides/authentication#webapp) and [follow the first step on this link to obtain your Spotify client_id and client_secret](https://developer.spotify.com/documentation/general/guides/app-settings/). Any email can be used to create these information
   * Under the OAuth screen on the left on the Google website, add the email you'd like the playlist to be in as a "Test User"
2. Fork this Github repository
3. Install the packages from the requirements.txt using pip
   * (Recommended) Create a virtual environment for this project before installing the packages using pip
4. Create a .env file in the same format as .env.example
   * Replace all of the 1111111111111111 with the respective client_id and client_secret. Keep these personal to yourself.
     * Note that these are NOT in quotes.
5. Run `app.py`. On Windows, it's `py app.py` in the terminal.
6. Go to `http://localhost:5000/` on your favorite browser.
7. Follow the directions on the web app below!
8. Exit out of the web app through the terminal.

# ...Why do I have to follow these directions? Especially step 1? <a name="why"></a>

Unfortunately, since this project is very early in development. Until we deploy it, you'd have to have a little bit of programming background to launch the local web app.

Due to limitations on how much data we can send to Google/YouTube, each user must provide their own YouTube/Google client_id and client_secrets. The Spotify versions of these are necessary as well since we haven't deployed our web app yet, so you shouldn't really use our client information. Hence, step 1.
