import requests
from bs4 import BeautifulSoup

url = "https://cenoteka.rs/proizvodi/mlecni-proizvodi/pavlaka"
response = requests.get(url)
doc = BeautifulSoup(response.content, 'html.parser')
cene = doc.find_all(text='Kisela pavlaka IMLEK Moja kravica 20%mm 180g')
parent = cene[0].parent.parent.parent
parent2 = cene[0].parent.parent.parent
children = parent.find_all('div','article-price flex-full-height-center border-gray-right text-center')
dicts = {}
for x in children:
    slika = x.find('img',alt=True)
    cena = x.find('div','price').text.strip()
    dicts[slika['alt']]=cena
min_key = [k for k, v in dicts.items() if v == min(dicts.values())]
