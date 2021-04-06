#!/usr/bin/env python3

from PIL import Image

def get_image(url):
    '''
    Should get a png image from internet
    '''
    pass

def post_img(image):
    '''
    Should post a img
    '''
    pass

def scat_image(output,
               real_png,
               position):
    
    real_png = Image.open(real_png)
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
    transparent.show()
    transparent.save(output)

if __name__ == '__main__':
    img2 = input('Please, the real png image: ')    
    img_output = input('Please, the output name: ')
    scat_image(
               f'poisoned {img_output}.png',
               img2,
               position=(0,0))