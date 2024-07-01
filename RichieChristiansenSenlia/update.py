import csv
import requests
temp = []
# with open('wikidata_image_3.csv', mode ='r',encoding="utf-8")as file:
#     csvFile = csv.reader(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for lines in csvFile:
#         # print(lines)
#         if(len(lines) > 0):
#             temp.append(lines)
pref = "http://127.0.0.1:3333/"
# temp = temp[1:]
# print(temp[0])
# print(temp)
# count = True
# for i in temp :
    # if(i[0]=="PakubuwanaI"):
    #     count = True
    # if(count):
        # print(i[0])
        # if(i[1] != "http://commons.wikimedia.org/wiki/Special:FilePath/default.png"):
data = {
        's':pref+"MapendumaNduga",
        'ns':pref+"Mapenduma"
        }
url = "https://historiografi.cs.ui.ac.id/db/rest/repositories/indonesia-history-ontology/sparql-templates/execute"
resp = requests.post(url,json=data)
print(resp)