import requests
from bs4 import BeautifulSoup

page = requests.get("https://www.nytimes.com")

html = page.text

soup = BeautifulSoup(html, "html.parser")

print(soup.find_all('span', 'balancedHeadline'))