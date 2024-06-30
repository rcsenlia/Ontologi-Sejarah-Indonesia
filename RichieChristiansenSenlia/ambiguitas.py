import csv
temp = []
with open('wikidata_id_2.csv', mode ='r',encoding="utf-8")as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        if(len(lines) > 0):
            temp.append(lines)

# print(temp)

head = set()
label = {}
temp = temp [1:]
print(temp[0])
iri = {}
for i in temp :
    if(i[1] in head):
        with open('map.csv','w',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([i[0],iri[i[1]]])
        
        
        continue
    else :
        head.add(i[1])
        label[i[1]] = i[2]
        iri[i[1]] = i[0]
print(len(temp))
print(len(head))

