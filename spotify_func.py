# Base 64 encoding for Spotify requests
import base64

# Requests library for Spotify API
import requests

# JSON for Spotify API parsin
import json

# Convert Spotify ClientID + ClientSecret to Base64 for Authorization
def convert_to_base64(clientid, clientsecret):
    message = clientid + ':' + clientsecret
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message

# Send Authorization request to Spotify and return access_token for search requests
# Lifetime of token is 3600 seconds (60 minutes) - Add refresh at some point
def receive_auth(clientid, clientsecret):
    base64_message = convert_to_base64(clientid, clientsecret)
    payload = {'grant_type': 'client_credentials'}
    url = 'https://accounts.spotify.com/api/token'
    headers = {'Authorization': 'Basic ' + base64_message}

    r = requests.post(url, data=payload, headers=headers)
    if 'error' in r.json():
        print('Error in Spotify ID or Secret')
        return 'Error'
    else:
        return r.json()['access_token']

# Album art search query - limit is at 1
def search_album_art(token, search):
    url = 'https://api.spotify.com/v1/search'
    params = {'q': search, 'type': 'album', 'limit': '1'}
    headers = {'Authorization': 'Bearer ' + token}
    r = requests.get(url, params=params, headers=headers)
    # Check if search returned anything - if not return generic image
    if len(r.json()['albums']['items']) == 0:
        return 'https://www.civhc.org/wp-content/uploads/2018/10/question-mark.png'
    else:
        return r.json()['albums']['items'][0]['images'][0]['url']
