import requests
import json

payload = {"name" : "Lei.Wang"}

#pass data as table
#response = requests.post("http://localhost:8080/greeting", data=payload)
#pass data as json
response = requests.post("http://localhost:8080/greeting", json=payload)
print(response.url)
print(response.text)
print(response.content)
print(response.json())