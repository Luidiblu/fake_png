#!/usr/bin/env python3

from io import BytesIO
from PIL import Image
import base64
import requests

def get_image(url):
    '''
    Should get a png image from internet
    https://pngtree.com/free-png
    '''
    return Image.open(requests.get(url, stream=True).raw)

def post_img_imgur(image):
    '''
    Should post a image on Imgur and return the URL
    '''
    im_file = BytesIO()
    image.save(im_file, format="PNG")
    base64_image = im_file.getvalue()
    
    url = "https://api.imgur.com/3/image"
    headers = {
        "Authorization": "Client-ID"
    }
    data = {
        "image": base64.,
        "name": "PNG",
        "title": "PNG",
        "description": "PNG"
    }
    data={
                'image': base64.b64encode(open(os.path.join(self.target_path, file_name), 'rb').read()),
                'type': 'base64',
                'name': file_name,
            }
    r = requests.post(url, headers=headers, data = data)

    print(r.text)
    return r.raw
# def post_img_pintrest(image):
#     '''
#     Should post a img
#     '''
#     api = pinterest.Pinterest(token=TOKEN)
#     board = api.board().create("Real Png", description="Real png images .png .PNG")
#     imgur_url = post_img_imgur(image)
#     api.pin().create(board, "Real png images .png .PNG")
#     pass

def scat_image(output,
               real_png_url,
               position):
    
    real_png = get_image(real_png_url)
    w, h = real_png.size

    white_img = Image.new("RGB", (w,h), "white")
    pixels = white_img.load()

    for i in range(w):
        for j in range(h):
            if (i + j) % 2:
                pixels[i, j] = (230, 230, 230)

    # TODO: Dependendo do tamanho da img, a gente altera o valor 13
    white_img = white_img.resize((13*w, 13*h), Image.NEAREST)

    transparent = Image.new('RGBA', (w, h), (0,0,0,0))
    transparent.paste(white_img, (0,0))
    transparent.paste(real_png, position, mask=real_png)
    transparent.show()
    transparent.save(output)
    return post_img_imgur(transparent)

if __name__ == '__main__':
    real_png_url = input('Please, the real png image: ')    
    img_output = input('Please, the output name: ')
    scat_image(f'poisoned {img_output}.png',
               real_png_url,
               position=(0,0))