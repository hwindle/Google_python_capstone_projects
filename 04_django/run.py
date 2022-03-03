#!/usr/bin/env python3

import os
import json, requests

def get_descriptions(src_dir):
    '''
    Returns a list of files from a dir.
    '''
    if not os.path.isdir(src_dir):
        print('You have not passed in a valid directory')
        sys.exit(1)
    text_files = []
    for root, d, f in os.walk(src_dir):
        for text_f in f:
            # append each file to list
            text_files.append(os.path.join(root, text_f))
    return text_files

def text_processing(text_files):
    if text_files == []:
        return False
    list_of_dicts = []
    number = 1 # counter for image name
    for f in text_files:
        one_fruit = {}
        with open(f) as file_handler:
            dirty_name = file_handler.readline()
            dirty_weight = file_handler.readline()
            dirty_desc = file_handler.readline()
            image_name = '00' + str(number) + '.jpg'
            name = str(dirty_name).strip('\n')
            one_fruit['name'] = name
            weight = int(dirty_weight[:-4])
            one_fruit['weight'] = weight
            desc = str(dirty_desc).strip('\n')
            one_fruit['description'] = desc
            one_fruit['image_name'] = 'supplier-data/images/' + image_name
        number += 1
        list_of_dicts.append(one_fruit)
        with open('fruits.json', 'w') as fruits_json:
            json.dump(list_of_dicts, fruits_json, indent = 4)
    return list_of_dicts

def post_data_website(list_of_dicts):
    for d in list_of_dicts:
        response =  requests.post('http://<ext-ip>/fruits/', d)
        if not response.ok:
            raise Exception('POST failed with status code of: {}'.format(response.status_code))
    print('POST succeeded')

description_list = get_descriptions('supplier-data/descriptions')
dicts = text_processing(description_list)
#print(dicts) # debug line
#post_data_website(dicts)
