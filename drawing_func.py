# Pillow Image Library
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

# Random # generation for file names
from random import seed
from random import randint

# Requests library for Downloading URL
import requests

seed(8008)

def draw(name):
    # Imported album art
    im = Image.open(name)
    im = im.resize((400, 400))

    # Empty background
    bg = Image.new('RGB', (800, 800), color = 'black');

    # Paste Images together
    bg.paste(im, (200,200))

    # Load in Pixel data
    px = bg.load()
    draw = ImageDraw.Draw(bg)

    # Fill in the corners
    # Top Left
    draw.rectangle([(0,0), (200,200)], fill = px[200,200])
    # Top Right
    draw.rectangle([(600,0), (800,200)], fill = px[599,200])
    # Bottom Left
    draw.rectangle([(0,600), (200,800)], fill = px[200,599])
    # Bottom Right
    draw.rectangle([(600,600), (800,800)], fill = px[599,599])

    # Draw from image edges
    for x in range(200, 600):
        # Top Row
        color = px[x, 200]
        draw.line((x, 200, x, 0), fill=color, width=1, joint=None)

        # Bottom Row
        color = px[x, 599]
        draw.line((x, 599, x, 800), fill=color, width=1, joint=None)

        # Left Side
        color = px[200, x]
        draw.line((200, x, 0, x), fill=color, width=1, joint=None)

        # Right Side
        color = px[599, x]
        draw.line((599, x, 800, x), fill=color, width=1, joint=None)

    # Blur image
    bg = bg.filter(ImageFilter.GaussianBlur(85))

    # Paste image back over blur
    bg.paste(im, (200,200))

    bg.show()
    bg.save('./output/' + str(randint(0, 9999999)) + '.jpg', quality=95, subsampling=0)

def draw_url(url):
    # Download Image using Requests
    img_data = requests.get(url).content
    with open('album_download.jpg', 'wb') as handler:
        handler.write(img_data)

    # Drawing function
    draw('album_download.jpg')
