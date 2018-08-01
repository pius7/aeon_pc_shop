# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from collections import defaultdict
import requests
from django.core.management.base import BaseCommand
from parts.models import parts_url

#get basic website for links to diffrent parts
class Command(BaseCommand):
    def crawl_urls(self):
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
        
        
        for part in listparts:
            for i in range(1,parts[part][1]+1):
                if i==1:
                    itemssoup = BeautifulSoup(requests.get(parts[part][0]).text, 'html.parser')
                    for item in itemssoup.find_all("div", {'class':'pcontent'}):
                        itemssoup = BeautifulSoup(requests.get(parts[part][0]).text, 'html.parser')
                        p=parts_url(name=item.find("div", {"class" : "pname"}).text, url=item.find("a", {"class" : "p-complete-link visible-xs visible-sm"})['href'], category=part)
                        p.save()
                else:
                    itemssoup = BeautifulSoup(requests.get(parts[part][0] + "/page/" + str(i)).text, 'html.parser')
                    for item in itemssoup.find_all("div", {'class':'pcontent'}):
                        itemssoup = BeautifulSoup(requests.get(parts[part][0]).text, 'html.parser')
                        p=parts_url(name=item.find("div", {"class" : "pname"}).text, url=item.find("a", {"class" : "p-complete-link visible-xs visible-sm"})['href'], category=part)
                        p.save()
                                
        
    def handle(self, *args, **options):
        self.crawl_urls()