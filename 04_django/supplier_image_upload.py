#!/usr/bin/env python3

import requests
import changeImage

url = 'http://localhost/upload/'
image_list = changeImage.get_image_list('supplier-data/images')

for image in image_list:
    with open(image, 'rb') as opened:
        r = requests.post(url, files = {'file': opened})
    print('end of for')
