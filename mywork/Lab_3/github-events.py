#!/home/codespace/.python/current/bin/python3

import os
import json
import requests

GHUSER = os.getenv('GITHUB_USER')
print(GHUSER)

url = 'https://api.github.com/users/yxs4yt/events'.format(GHUSER)
print(url)

r = json.loads(requests.get(url).text)

for x in r[:5]:
  event = x['type'] + ' :: ' + x['repo']['name']
  print(event)
print (r)
