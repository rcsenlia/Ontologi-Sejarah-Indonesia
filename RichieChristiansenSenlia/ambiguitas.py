import csv
temp = []
with open('wikidata_id.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        if(len(lines) > 0):
            temp.append(lines)

# print(temp)

head = set()
label = {}
temp = temp [1:]
print(temp[0])
for i in temp :
    if(i[1] in head):
        print(i[1],i[2])
        continue
    else :
        head.add(i[1])
        label[i[1]] = i[2]
print(len(temp))
print(len(head))

