import requests
import csv
import urllib.parse
data = requests.get('https://historiografi.cs.ui.ac.id/api/map/all').json()
res = []
# for i in data :
#     try:
#         temp = requests.get('http://localhost:8000/api/graph/image/'+urllib.parse.quote(i['name'])).json()
#         if('response' in temp):
#             continue
#     except:
#         continue
#     res.append({'iri':i['iri'],
#                 'image':temp['image']})

# with open('wikidata_image.csv','w',encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['iri','image'])
#     for i in res :
#         writer.writerow([i['iri'],i['image']])
res = []
for i in data :
    try:
        temp = requests.get('http://localhost:8000/api/graph/alias/'+urllib.parse.quote(i['name'])).json()
        if('response' in temp):
            continue
    except:
        continue
    res.append({'iri':i['iri'],
                'alias':temp['alias']})

with open('wikidata_alias.csv','w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['iri','alias'])
    for i in res :
        for j in i['alias']:
            writer.writerow([i['iri'],j])
