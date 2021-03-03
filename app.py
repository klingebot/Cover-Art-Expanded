# Environment variables for Spotify
import os
from dotenv import load_dotenv
load_dotenv()

# Import Spotify functions
from spotify_func import *

# Drawing functions
from drawing_func import *

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

if len(client_id) != 0:
    print("Using Spotify")
    while True:
        search = input('Enter an album name: ')
        # Receive Auth from Spotify
        access_token = receive_auth(client_id, client_secret)
        if (access_token != 'Error'):
            # Search image from Spotify API
            search_image = search_album_art(access_token, search)

            draw_url(search_image)
else:
    print("Not Using Spotify - Defaulting to Album.jpg")
    draw('album.jpg')
