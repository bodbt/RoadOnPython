import requests

response = requests.get("http://localhost:8080/greeting")

print(response.status_code)
print(response.reason)

for name, value in response.headers.items():
    print("%s:%s" % (name, value))

print(response.content)

args = {"name" : "Lei.Wang"}
response = requests.get("http://localhost:8080/greeting", params=args)
print(response.url)
print(response.content)
