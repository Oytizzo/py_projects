import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

questions = soup.select(".question-summary")

print(type(questions[0]))
print(type(questions[0].attrs))
print(questions[0].attrs)