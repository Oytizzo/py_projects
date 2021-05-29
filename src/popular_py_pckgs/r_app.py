import requests

url = "https://imgs.xkcd.com/comics/python.png"

r = requests.get(url)

with open('comic.png', 'wb') as f:
    f.write(r.content)
