import csv
temp = []
with open('map_final.csv', mode ='r',encoding="utf-8")as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)