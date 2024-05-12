import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Sachin_Tendulkar"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

image_links = [ img['src'] for img in soup.find_all('img') ]

image_links =  image_links[:10]

cntr = 1
for link in image_links:
    print(f"{cntr}. ",link)
    cntr+=1