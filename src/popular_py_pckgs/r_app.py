import requests

payload = {'username': 'david', 'password': 'testing123'}
url = "https://httpbin.org/post"

r = requests.post(url, data=payload)

print(r.status_code)
print(r.ok)
print(r.headers)
print(r.text)
