import requests
import re

username="name"
password="123"

s = requests.Session()
#pass data as table
s.post("http://login_url", data=(username, password))
#access home url after login
r = s.get("http://home_url")
print(r.url)
print(r.text)
print(r.content)
print(r.json())

s.close()

"""
BeatifulSoup4 package is a HTML.parser.
"""