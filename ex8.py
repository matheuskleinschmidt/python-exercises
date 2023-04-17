import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

for title in soup.find_all('h2', {'class': 'css-1vvhd4r e1voiwgp0'}):
    print(title.text)
