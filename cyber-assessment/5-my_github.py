#!/usr/bin/python3
import requests
import sys

username = sys.argv[1]

r = requests.get(f'https://api.github.com/users/{username}')
print(r.json()['id'])
