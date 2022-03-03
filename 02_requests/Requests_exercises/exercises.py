#!/usr/bin/env python3

import requests

response = requests.get('https://www.google.com')
print(response.text[:300])
response.request.headers['Accept-Encoding']
'gzip, deflate'
