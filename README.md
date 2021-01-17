## Introducing, You-tify!

This was a submission for the SB Hacks VII Hackathon. Our Devpost can be found here. (link to come later)

## Inspiration

Dylan recently started learning Python a month ago and, while coding, he often turned on music on Spotify. Recently, he has been listening to some game soundtracks. Unfortunately, Spotify's selection of select game music is sorely lacking! He created a YouTube playlist and found a far better selection of more YouTube-exclusive songs and remixes. However, he wanted to also import his previous Spotify playlist onto that same platform.

But importing his large, 30+ song playlist would be tedious! He also was interested in learning how to use a Web API as well. The perfect solution? Utilize Spotify and YouTube APIs to accomplish this task! Thus, the idea for You-tify was born, with Dylan, Jennifer, Thomas, and Vince attempting to make it a reality during SB Hacks VII.

## What it does

You-tify takes in a public Spotify Playlist link and, after giving the program access to your account, creates a playlist of the same songs! When you launch the local Web App, you'll be able to paste the Spotify playlist link and then, when you click the URL the application gives, you'll be taken to your transferred playlist!

## How we built it

Dylan and Jennifer handled most of the backend. For the Spotify API call, we used a Python library called spotipy. For the YouTube API calls, Google's libraries for Python were used, such as Google APIs Client Library for Python (google-api-python-client) and google-auth-oauthlib.

Thomas and Vince worked on the frontend. The frontend consists of the Flask framework in Python, with some CSS from Bootstrap.

## Challenges we ran into

Dylan: I have never worked with any Web APIs before, so it was an interesting challenge familiarizing myself with the YouTube API's documentation in such a limited time. Additionally, figuring out OAuth 2 made this far more difficult as well. I also used this hackathon as an opportunity to learn VS Code (I've only used PyCharm for Python) and introducing myself to Git/GitHub to collaborate with a team on future projects.

Jennifer: I have never worked with Web APIs and Git/GitHub before either, so learning how to use them was a good challenge. Also, the response body of the playlist_item() request contains an array of track objects wrapped in a paging object in JSON format. Figuring out how to make this into the desired list of dictionaries was a good exercise.

Thomas: It was my first time using Flask, but I found the actual framework pretty simple to get used to. Not so simple, however, was getting it to work. I had no experience with pip or dealing with large numbers of Python dependencies, and the boilerplate code we started from ended up being rather excessively complex for our uses. It was a good exercise in adapting to a new coding environment.

Vince: I got stuck on the very beginning for 3 hours trying to install flask.

## Accomplishments that we're proud of

Dylan: After struggling to figure out how to successfully authorize myself after a couple hours of getting frustrating errors, making my first ever API call was incredibly satisfying. And seeing the entire project slowly build up over the hackathon and the final connection between frontend and backend: amazing.

Jennifer: Successfully setting up user authentication to the Spotify Web API and getting the playlist retrieval function to work was rewarding. I am proud that the team finalized this app so well.

Thomas: To be honest, when Dylan told me his idea I was a little skeptical that we four hackathon beginners could pull it off. It was immensely satisfying to finally get the app working and fulfilling the original idea after struggling with it for a great deal.

Vince: I'm proud that I went from knowing nothing about flask at the beginning of the hackathon to knowing a little more about flask at the end.

## What we each learned

Dylan: I learned how to really deep dive into documentation of Web APIs, utilizing the basics of Git (Thanks Tommy), and using VS code. PyCharm automatically initializes virtual environments for you, so learning how to create a virtual environment in VS code was amazing. Additionally, I've never developed an intense project and learned something this new in such a short amount of time.

Jennifer: I learned about Spotipy, Spotify data documentation, nested dictionaries, Git commands, and front/back-end development.

Thomas: One big thing I learned was to trust in my team members. I tend to want to go over every line and understand everything, but there was no time to do that here. I was blown away by how well we worked together, considering I had never met any of them before. I'd love to work with them again!

Vince: The most valuable thing I learned from this hackathon was how to use Git.  I can do the basics now!  (Thanks Tommy)

## What's next for You-tify?

As we are still all beginners, there is a lot of room for growth for this project. There is a quota limit for calling the YouTube API, so the program is highly limited on the number of songs that you can transfer over each day (less than 100). The app on Google console could potentially be published to avoid the "untrusted app" message users get when they try to authorize the web app. And, not every user can use You-tify since their email must be added as a registered "test user," so there is a hard limit of 100 possible unique users at the moment. This issue, however, can be fixed if every person creates their own .env file with their own Spotify and YouTube client_ID and client_secrets.

Due to the time limitations, we were also unable to finish deploying the web application on Heroku, which is something we'd like to have done to elevate our final product further. Additionally, the playlist creation API call makes a new playlist every time; we could develop a smarter backend to see if a duplicate playlist exists and update it with any new songs from Spotify to synchronize the two platforms. Lastly, from this experience, we would definitely be able to develop our idea and go the reverse route. Imagine, the sibling of You-tify: Spoti-tube?
