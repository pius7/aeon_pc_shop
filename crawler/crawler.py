from bs4 import BeautifulSoup
from django.db import migrations
from collections import defaultdict
import requests
#get basic website for links to diffrent parts

main = BeautifulSoup(requests.get('https://www.mindfactory.de/').text, 'html.parser')

hardwarerequest = requests.get(main.find("a", {'title':'Hardware'})['href'])
hardware = BeautifulSoup(hardwarerequest.text, 'html.parser')

parts=defaultdict(list)
listparts=("Prozessor" ,"Grafikkarte", "Mainboard" , "Arbeitsspeicher" , "Festplatte", "Kühlung Luft", "Kühlung Wasser", "Gehäuse", "Laufwerke", "Netzteile", "SSD", "Netzwerk")

# get urls and number of pages per category


for part in listparts:
    for cat in hardware.find_all('a'):
        if part == "Kühlung Luft":
            if str(cat.get('title')).find("Luft") != -1:
                parts.setdefault(part, []).append(cat.get('href'))
                break   
        elif part == "Kühlung Wasser":
            if str(cat.get('title')).find("Wasser") != -1:
                parts.setdefault(part, []).append(cat.get('href'))
                break
        elif part == "SSD":
            if str(cat.get('title')).find("Solid") != -1:
                parts.setdefault(part, []).append(cat.get('href'))
                break
        else:
            if str(cat.get('title')).find(part) != -1:
                parts.setdefault(part, []).append(cat.get('href'))
                break
            
for part in listparts:
    if part == "Netzwerk":
        parts[part].append(1)
        continue
    else:
        partsoup = BeautifulSoup(requests.get(parts[part][0]).text, 'html.parser')
        pagination = partsoup.find("ul", {'class': 'pagination pull-right'}).text
        pagesnr = [int(s) for s in pagination.split() if s.isdigit()]
        parts[part].append(pagesnr[1])


# for part in listparts:
part = "Netzwerk"
for i in range(1,parts[part][1]+1):
    if i == 1:
        itemssoup = BeautifulSoup(requests.get(parts[part][0]).text, 'html.parser')
        items=itemssoup.find_all("div", {'class':'p'})
        for item in items:
            print(item)
    else:
        itemssoup = BeautifulSoup(requests.get(parts[part][0] + "page/" + str(i) + '/').text, 'html.parser')
        print (itemssoup.href)