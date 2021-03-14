# Cover-Art-Expanded
Python script to add a new dimension to Album/Cover Art by expanding upon the edge.

Image manipulation done with the Pillow Library (Fork of PIL)

# Usage
## Requirements
Pillow Library, Dotenv, Requests, Base64, Json
## Executing
Run app.py with either Spotify or imported images in mind. Usage for both is found below.
### Spotify
If using Spotify, add your Spotify credentials (Client ID, Client Secret) into the environment file. (https://developer.spotify.com/dashboard) The script will default to Spotify and take care of the Client Credential flow to allow for automatic searching and formatting.
### Imported Images
Add in any JPG into the base folder and name it, 'album.jpg'. Leave environment variables empty to allow script to disable Spotify searching.
# Examples
## Example Input
![Input Image](/examples/input.jpg)
## Example Output
![Input Image](/examples/output.jpg)
