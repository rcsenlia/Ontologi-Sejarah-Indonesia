import wikipedia
import csv
wikipedia.set_lang('id')

temp = []
cnt = 0
with open('query-result.csv', mode ='r',encoding="utf-8")as file:
    
    
    csvFile = csv.reader(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for lines in csvFile:
        print(cnt)
        cnt = cnt + 1
        # print(lines)
        
        # title = wikipedia.search(lines[2])[0]
        # print(title)
        try:
            title = wikipedia.search(lines[2])[0]
            print(title)
            page = wikipedia.page(title)
            try:
                image = page.images[0]
            except:
                image = ""
            url = page.url
            summary = wikipedia.summary(title,sentences=5)
            temp.append([lines[0],url,image,summary])
        except:
            pass
pref = "http://127.0.0.1:3333/"
temp = temp[1:]
print(temp[0])

with open('wikidata_article_title.csv','w',encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['iri','wikiurl','image','summary'])
    for i in temp:
        writer.writerow(i)
