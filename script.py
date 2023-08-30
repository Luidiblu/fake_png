#!/usr/bin/env python3

from io import BytesIO
from PIL import Image
import base64
import requests


def get_image(url: str) -> Image:
    '''
    Fetches a png image from the given URL and returns it as an Image object.
    '''
    return Image.open(requests.get(url, stream=True).raw)


def scat_image(output: str,
               real_png_url: str,
               position: tuple) -> None:
    '''
    Creates a white image with a chessboard pattern, resizes it, pastes a real PNG image on it at the given position, and saves the result.
    '''
    
    real_png = get_image(real_png_url)
    w, h = real_png.size

    white_img = Image.new("RGB", (w,h), "white")
    pixels = white_img.load()

    for i in range(w):
        for j in range(h):
            if (i + j) % 2:
                pixels[i, j] = (230, 230, 230)

    white_img = white_img.resize((13*w, 13*h), Image.NEAREST)

    transparent = Image.new('RGBA', (w, h), (0,0,0,0))
    transparent.paste(white_img, (0,0))
    transparent.paste(real_png, position, mask=real_png)
    transparent.save(output)

if __name__ == '__main__':
    '''
    Takes user input for the real PNG URL and the output file name, and then calls the scat_image function with these inputs and a fixed position.
    '''
    real_png_url = input('Please, the real URL png image: ')    
    img_output = input("Please, the output name (name will come with poisoned_YOUR_INPUT): ")
    scat_image(f'poisoned {img_output}.png',
               real_png_url,
               position=(0,0))