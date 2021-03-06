import requests
from bs4 import BeautifulSoup

a = requests.get('https://leagueoflegends.fandom.com/wiki/List_of_champions')
html = BeautifulSoup(a.text, 'html.parser')

title = html.find('h1', attrs={'class': 'page-header__title'}).text.strip()

aside = html.find('div', attrs={'class': 'mw-parser-output'})
for description in aside:
    description = aside.find('p').text.strip()

results = html.find('table', attrs={'class': 'article-table sticky-header sortable'})

rows = results.find_all('span', attrs={'class': 'inline-image'})
records = []
for row in rows:
    line = row.find('a').get_text(separator='\n')
    records.append(line.split("\n", 1))

"""
dictionary = {}
keys = []
values = []

for i in records:
    keys[i] = records[i][0]
    values[i] = records[0][i]

    for key, value in zip(keys, values):
        dictionary[key] = value

print(dictionary)

j'ai essayé de créer un dictionnaire avec ma liste mais je n'ai pas réussi.
l'idée était de faire une requête utilisateur avec un input pour demander pour quel champion on veut récupérer les informations.
Je n'ai malheureusement pas réussi à récupérer le get text() directement du tr pour une raison inconnue
"""
print(title)
print(description)
print(records)
