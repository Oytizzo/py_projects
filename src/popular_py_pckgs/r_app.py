import requests

payload = {'page': 2, 'count': 25}
url = "https://httpbin.org/get"

r = requests.get(url, params=payload)

print(r.status_code)
print(r.ok)
print(r.headers)
print(r.url)
