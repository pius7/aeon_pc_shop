#!/usr/bin/python
# -*- coding: utf -*-

from bs4 import BeautifulSoup
from django.db import migrations
from collections import defaultdict
import requests
from parts.models import parts_urls

#get basic website for links to diffrent parts
def crawl_urls():
    main = BeautifulSoup(requests.get('https://www.mindfactory.de/').text, 'html.parser')
    
    hardwarerequest = requests.get(main.find("a", {'title':'Hardware'})['href'])
    hardware = BeautifulSoup(hardwarerequest.text, 'html.parser')
    
    parts=defaultdict(list)
    items=defaultdict(list)
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
    
    
    #for part in listparts:
    for i in range(1,parts[part][1]+1):
        itemssoup = BeautifulSoup(requests.get(parts[part][0]).text, 'html.parser')
        if len(itemssoup.find_all("div", {'class':'pcontent'}))<30:
            for x in range(0,len(itemssoup.find_all("div", {'class':'pcontent'}))):
                item=itemssoup.find_all("div", {'class':'pcontent'})[x]
                items.setdefault(part, []).append(item.find("div", {"class" : "pname"}).text)
                items[part].append(item.find("a", {"class" : "p-complete-link visible-xs visible-sm"})['href'])
        else:
            itemssoup = BeautifulSoup(requests.get(parts[part][0] + "page/" + str(i) + '/').text, 'html.parser')
            for x in range(0,len(itemssoup.find_all("div", {'class':'pcontent'}))):
                item=itemssoup.find_all("div", {'class':'pcontent'})[x]
                items.setdefault(part, []).append(item.find("div", {"class" : "pname"}).text)
                items[part].append(item.find("a", {"class" : "p-complete-link visible-xs visible-sm"})['href'])
    
    return items