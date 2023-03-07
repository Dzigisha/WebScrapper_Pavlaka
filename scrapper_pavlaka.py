# from bs4 import BeautifulSoup
# import requests

# url = "https://cenoteka.rs/proizvodi/mlecni-proizvodi/pavlaka"
# result = requests.get(url)
# doc = BeautifulSoup(result.text,"html.parser")
# rez = doc.find_all("Kisela pavlaka IMLEK Moja kravica 20%mm 400g")
# print(rez)
import requests
from bs4 import BeautifulSoup

# The URL of the page we want to scrape
url = "https://cenoteka.rs/proizvodi/mlecni-proizvodi/pavlaka"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page using Beautiful Soup
doc = BeautifulSoup(response.content, 'html.parser')

# Find all the products listed on the page
# products = soup.find_all('section', class_='row section list-articles-content box-shadow bg-white')
cene = doc.find_all(text='Kisela pavlaka IMLEK Moja kravica 20%mm 400g')
parent = cene[0].parent.parent.parent
children = parent.find('div','price lowest akcija star-top p-0')

print(children.text)