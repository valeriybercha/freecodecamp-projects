import requests                     # pip install requests
from bs4 import BeautifulSoup       # pip install beautifulsoup4


# Simple request with 'request' python module
res = requests.get('https://w3schools.com/python/demopage.htm')
print(res.status_code) # printing server response
print(res.text) # printing html page


# Simple requests with 'BeautifulSoup' module
page = requests.get("http://valeriybercha.com/")
soup = BeautifulSoup(page.content, 'html.parser')
page_title = soup.title.text # Extracting title of the page
page_head = soup.head # Extracting head of the page 
page_body = soup.body # Extracting body of the page

print(page_body)