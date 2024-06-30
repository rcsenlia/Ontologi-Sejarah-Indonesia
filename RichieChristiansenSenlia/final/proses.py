import csv

file_path = 'date-actor-all.csv'
data = []
with open(file_path, newline='',encoding='UTF-8') as f:
    reader = csv.reader(f, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        if(len(row)>1):
            data.append(row)

dup = set()


with open('date_no_duplicate_actor.csv','w',encoding='utf-8') as file:
    writer = csv.writer(file)
    
    for i in data :
        if(i[0] in dup):
            print(i[0])
            continue
        else:
            writer.writerow(i)
            dup.add(i[0])

print(len(dup))
print(len(data))

#date untuk infobox politican belum standard
#date untuk prime minister
#date former country perlu di cek

#file prime minister sama politician belum di proses