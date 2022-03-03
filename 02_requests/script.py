#!/usr/bin/env python3

import os
import requests

def create_dictionary(text_file, index):
    '''
    Paramaters: one text file path

    Returns: a dictionary with title, name,
    date, and feedback
    '''
    file_dict = {}
    with open(text_file, 'r') as text:
        file_dict['id'] = index
        file_dict['title'] = text.readline()
        file_dict['name'] = text.readline()
        file_dict['date'] = text.readline()
        file_dict['feedback'] = text.readline()
    print(file_dict)
    return file_dict



text_files_list = os.listdir('/data/feedback')
index = 1

for f in text_files_list:
    file_dict = create_dictionary(f, index)
    index += index
    # request.post() with dict.
    response =  requests.post('http://34.121.192.162/feedback/', file_dict)
    if not response.ok:
        raise Exception('POST failed with status code of: {}'.format(response.status_code))
    else:
        print('POST succeeded')
