import requests
import csv
import urllib.parse
data = requests.get('http://localhost:8000/api/graph/all').json()
res = []
cnt = 0
print(len(data))
#id
# for i in data :
#     print(cnt)
#     cnt += 1
#     try:
#         temp = requests.get('http://localhost:8000/api/graph/id/'+urllib.parse.quote(i['name'])).json()
#         if('response' in temp):
#             continue
#     except:
#         continue
#     res.append({'iri':i['iri'],
#                 'id':temp['id'],
#                 'label':temp['label']})

# with open('wikidata_id.csv','w',encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['iri','id'])
#     for i in res :
#         writer.writerow([i['iri'],i['id'],i['label']])

#image

# for i in data :
#     print(cnt)
#     cnt += 1
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

#alias

for i in data :
    print(cnt)
    cnt += 1
    try:
        temp = requests.get('http://localhost:8000/api/graph/alias/'+urllib.parse.quote(i['name'])).json()
        if('response' in temp):
            continue
    except:
        continue
    # print(temp)
    res.append({'iri':i['iri'],
                'alias':temp['alias']})

with open('wikidata_alias.csv','w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['iri','alias'])
    for i in res :
        for j in i['alias']:
            writer.writerow([i['iri'],j['value']])
