#!/usr/bin/env python3

import json
from datetime import date
import reports, emails

def process_data(json_file):
    title = 'Processed Update on ' + date.today().strftime("%d/%m/%Y")
    try:
        with open(json_file) as file_handler:
            data = json.load(file_handler)
        fruits_description = ''
        for fruit in data:
            fruits_description += 'name: ' + fruit['name']
            fruits_description += '<br/>'
            fruits_description += 'weight: ' + str(fruit['weight']) + ' lbs'
            fruits_description += '<br/><br/>'
    except ValueError as e:
        print('That JSON filename is invalid, {}'.format(e))
        return False
    reports.generate_report('processed.pdf', title, fruits_description)
    return True


if __name__ == '__main__':
    process_data('fruits.json')
    msg = emails.generate_email(
        'automation@example.com',
        'username@example.com',
        'Upload Completed - Online Fruit Store',
        'All fruits are uploaded to our website successfully. A detailed list is attached to this email.',
        '/tmp/processed.pdf'
    )
    emails.send_email(msg)
