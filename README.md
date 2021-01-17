## Introducing, You-tify!

This was a submission for the SB Hacks VII Hackathon. Our Devpost can be found here. (link to come later)

## Inspiration

Dylan recently started learning Python a month ago and, while coding, he often turned on music on Spotify. Recently, he has been listening to some game soundtracks. Unfortunately, Spotify's selection of game music is sorely lacking! He created a YouTube playlist and found a far better selection of more YouTube-exclusive songs and remixes. However, he wanted to also import his previous Spotify playlist onto that same platform.

But importing his large, 50+ song would be tedious! He also was interested in learning how to use a Web API as well. The perfect solution? Utilize Spotify and YouTube APIs to accomplish this task! Thus, the idea for You-tify was born, with Dylan, Jennifer, Thomas, and Vince attempting to make it a reality during SB Hacks VII.

## What it does

You-tify takes in a public Spotify URL and, after giving the program access to your account, creates a playlist of the same songs!

## How we built it

Dylan and Jennifer handled most of the backend.

Thomas and Vince worked on the frontend. The frontend consists of the Flask framework in Python, with CSS from Bootstrap.

## Challenges we ran into

Dylan: I have never worked with any Web APIs before, so it was an interesting challenge familiarizing myself with the YouTube data documentation in such a limited time. Additionally, figuring out OAuth 2 made this far more difficult as well. I also used this hackathon as an opportunity to learn VS Code (I've only used PyCharm for Python) and introducing myself to Git/GitHub to collaborate with a team on future projects.

Jennifer: I have never worked with Web APIs and Git/GitHub before either, so learning how to use them was a good challenge. After creating an app through the Spotify for Developers website, I did not want to immortalize the app credentials in my source code because I figured our client secret should remain secret, but setting environment variables in my terminal did not seem to work so I ended up passing them through the Client Credential Flow directly. Also, the response body of the playlist_item() request contains an array of track objects wrapped in a paging object in JSON format. Figuring out how to make this into a readable list of dictionaries in the data structure Dylan wanted was a good exercise.

Thomas: It was my first time using Flask, but I found the actual framework pretty simple to get used to. Not so simple, however, was getting it to work. I had no experience with pip or dealing with large numbers of Python dependencies, and the boilerplate code we started from ended up being rather excessively complex for our uses. It was a good exercise in adapting to a new coding environment.

Vince: I got stuck on the very beginning for 3 hours trying to install flask.

## Accomplishments that we're proud of

Dylan: After struggling to figure out how to successfully authorize myself after a couple hours of getting frustrating errors, making my first ever API call was incredibly satisfying.

Jennifer: Successfully setting up user authentication to the Spotify Web API and defining a "get playlist name & tracks" function with an appropriate path parameter was rewarding.

Thomas: To be honest, when Dylan told me his idea I was a little skeptical that we four hackathon beginners could pull it off. It was immensely satisfying to finally get the app working and fulfilling the original idea after struggling with it for a great deal.

Vince: I'm proud that I went from knowing nothing about flask at the beginning of the hackathon to knowing a little more about flask at the end.

## What we each learned

Dylan: I learned how to really deep dive into documentation of Web APIs, utilizing the basics of Git, and using VS code.

Jennifer: I learned about Spotipy, Spotify data documentation, nested dictionaries, git commands, the 're' module, and front/back-end development.

Thomas: One big thing I learned was to trust in my team members. I tend to want to go over every line and understand everything, but there was no time to do that here. I was blown away by how well we worked together, considering I had never met any of them before. I'd love to work with them again!

Vince: The most valuable thing I learned from this Hackathon was how to use git.  I can do the basics now!  (Thanks Tommy)

## What's next for You-tify?


