import requests
import csv
import urllib.parse
data = requests.get('http://localhost:8000/api/graph/all').json()
res = []
cnt = 0
print(len(data))
# id
# for i in data :
#     print(cnt)
#     cnt += 1
#     try:
#         temp = requests.get('http://localhost:8000/api/graph/image/'+urllib.parse.quote(i['name'][10:])).json()
#         if('response' in temp):
#             continue
#     except:
#         continue
#     res.append({'iri':i['iri'],
#                 'image':temp['image'],
#                 'wikilinks':temp['wikilinks']})

# with open('wikidata_image_3.csv','w',encoding='utf-8') as file:
#     writer = csv.writer(file)
#     writer.writerow(['iri','id'])
#     for i in res :
#         writer.writerow([i['iri'],i['image'],i['wikilinks']])

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
    # if(cnt==10):
    #     break
    try:
        temp = requests.get('http://localhost:8000/api/graph/image/'+urllib.parse.quote(i['name'])).json()
        if('response' in temp):
            continue
    except:
        continue
    print(temp)
    res.append({'iri':i['iri'],
                'alias':temp['alias']})

with open('wikidata_alias_2.csv','w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['iri','alias'])
    for i in res :
        for j in i['alias']:
            writer.writerow([i['iri'],j['value']])
