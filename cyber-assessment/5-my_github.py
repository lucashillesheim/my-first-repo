#!/usr/bin/python3
import requests
import sys

p = sys.argv[2]
headers = {'Authorization': f'Bearer {p}'}

r = requests.get(f'https://api.github.com/user', headers=headers)
if r.status_code == 200:
    print(r.json()['id'])
else:
    print(None)
