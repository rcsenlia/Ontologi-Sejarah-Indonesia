import csv

file_path = 'person cleaned.csv'
data = []
with open(file_path, newline='', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in reader:
        # if(len(row)>5):
        data.append([row[0],row[5].split("\r")])

print(data)
data = data[1:]

with open('judah_relatives.csv','a',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['key','relatives'])
    for i in data :
        for j in i[1] :
            writer.writerow([i[0],j.replace("\n","")])

#date untuk infobox politican belum standard
#date untuk prime minister
#date former country perlu di cek

#file prime minister sama politician belum di proses