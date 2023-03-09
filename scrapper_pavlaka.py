import requests
from bs4 import BeautifulSoup
from datetime import date
import csv

today = date.today()
url = "https://cenoteka.rs/proizvodi/mlecni-proizvodi/pavlaka"
response = requests.get(url)
doc = BeautifulSoup(response.content, 'html.parser')
ime_proizvoda='Kisela pavlaka IMLEK Moja kravica 20%mm 180g'
cene = doc.find_all(string='Kisela pavlaka IMLEK Moja kravica 20%mm 180g')
parent = cene[0].parent.parent.parent
parent2 = cene[0].parent.parent.parent
children = parent.find_all('div','article-price flex-full-height-center border-gray-right text-center')
dicts = {}
for x in children:
    slika = x.find('img',alt=True)
    cena = x.find('div','price').text.strip()
    dicts[slika['alt']]=cena
min_key = [k for k, v in dicts.items() if v == min(dicts.values())]
print("Radnje koje danas imaju popust na "+ime_proizvoda)
for i in min_key:
    print(i+" "+dicts[i]+"rsd")
d1 = today.strftime("%d/%m/%Y")
print(d1)
new_row={'datum':d1,'proizvod':ime_proizvoda,'cena':dicts[min_key[0]],'radnje':min_key,}
filename = 'pavlaka_tabela.csv'
header = ['datum','proizvod', 'cena', 'radnje']
with open(filename, 'a', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=header)
    if csvfile.tell() == 0:
        writer.writeheader()
    writer.writerow(new_row)