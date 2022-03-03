#!/usr/bin/env python3

from PIL import Image
import os, sys

def get_image_list(src_dir):
    '''
    Look for images in the given directory,
    and return a list of image path URI's
    '''
    # if src dir not a dir
    if not os.path.isdir(src_dir):
        print('You have not passed in a valid directory')
        # print error and exit.
        sys.exit(1)

    # Look through dir, for *.jpg and *.png imgs
    image_list = []
    for root, d, imgs in os.walk(src_dir):
        for picture in imgs:
            if picture.endswith('.jpg') or picture.endswith('.png'):
                # append each img to list
                image_list.append(os.path.join(root, picture))
    return image_list


def alter_pics(dest_dir, image_list):
    '''
    Parameters are the destination folder for the
    pictures, and an image_list with relative paths
    to the images.

    returns True if done
    '''
    number = 0
    for img in image_list:
        # open image
        new_pic_name = '0' + str(number) + '.png'
        new_filename = os.path.join(os.getcwd(), dest_dir, new_pic_name)
        number += 1
        #print(new_filename)
        try:
            with Image.open(img) as i:
                # resize, rotate image
                smaller = i.resize((256, 256)).rotate(90)
                # save image as PNG to dest_dir
                smaller.save(new_filename, 'PNG')
        except ValueError:
            print('That hasn\'t worked')
            return False

    return True


# dest for modified pictures
dest_dir = 'dest_pics'
images = get_image_list('src_pics')
alter_pics(dest_dir, images)
