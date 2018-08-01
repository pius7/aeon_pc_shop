# -*- coding: utf-8 -*-

import requests, tempfile, re, datetime, decimal

from bs4 import BeautifulSoup
from collections import defaultdict
from django.core.management.base import BaseCommand
from parts.models import part, parts_url
from PIL import Image
from django.core import files



class Command(BaseCommand):
    def crawl_product_info(self):
        
        all_products = parts_url.objects.all()
        for product in all_products:
        #product=all_products[1207]
        #product=parts_url.objects.filter(url="https://www.mindfactory.de/product_info.php/12000GB-LaCie-2big-Dock-STGB12000400-3-5Zoll--8-9cm--1x-DisplayPort-2x-_1199247.html")[0]
        #print(product.url)
        #print (product.name)
            
            url = product.url
        
            product_site = BeautifulSoup(requests.get(url).text, 'html.parser')
            
            try:
                x = product_site.find("div", {'class':'not_available_anymore'}).find("h4").text
            except:
                image_url = product_site.find("div", {'id':'bImageCarousel'}).find("div", {'class':'item active'}).find("img")['src']
                
                try:
                    price = decimal.Decimal(re.search(r'\d+\,\d+', product_site.find("div", {'class':'pprice'}).find("span", {'class': 'specialPriceText'}).text).group().replace(',', '.'))
                except AttributeError:
                    try:
                        price = decimal.Decimal(re.search(r'\d+\,\d+', product_site.find("div", {'class':'pprice'}).text).group().replace(',', '.'))
                    except AttributeError:
                        price = decimal.Decimal(re.search(r'\d+', product_site.find("div", {'class':'pprice'}).text).group().replace(',', '.'))
                description = product_site.find("p", {'itemprop':'description'}).text
                rating = 1
                try:
                    item_specs_table = product_site.find("table", {'class':'table table-striped table-hover'}).findAll("tr")
                    specs =[]
                    specs_categorys = []
                    specs_values = []
                    for setoflines in item_specs_table:
                        for lines in setoflines.findAll("td"):
                            for line in  lines:
                                specs.append(line)
                    
                    for x, spec in enumerate(specs):
                        if x %2 ==0:
                            specs_categorys.append(specs[x])
                        else:
                            specs_values.append(specs[x])
                except AttributeError:
                    specs_categorys = []
                    specs_values = []
                    
                
                availability_information = product_site.find("div" ,{'class', 'pshipping'}).find("a").text
                availability = re.sub("[^\w]", " ",  availability_information).split()
                if availability[0] == "Bestellt":
                    if (availability[1]=="Ohne") & (availability[2]=="Liefertermin"):
                        available_amount=0
                        available_from = (datetime.datetime.now() + datetime.timedelta(days=4)).strftime("%Y-%m-%d")
                    else:
                        date_available=re.search(r'\d{'+str(len(availability[3]))+'}.\d{'+str(len(availability[4]))+'}.\d{'+str(len(availability[5]))+'}', availability_information).group()
                        available_amount = 0
                        available_from = datetime.datetime.strptime(date_available, '%d.%m.%Y').strftime("%Y-%m-%d")
                elif availability[0] =="Lagernd":
                    available_amount =availability[1]
                    available_from = datetime.datetime.now().strftime("%Y-%m-%d")
                    try:
                        if availability[3] == '1':
                            available_amount = 1
                            available_from = datetime.datetime.now().strftime("%Y-%m-%d")
                    except IndexError:
                        pass
                elif availability[0] =="Verfügbar":
                    available_amount =1
                    available_from = datetime.datetime.now().strftime("%Y-%m-%d")
                elif (availability[0]=="Ohne") & (availability[1]=="Liefertermin"):
                    available_amount = 0
                    available_from= (datetime.datetime.now() + datetime.timedelta(days=14)).strftime("%Y-%m-%d")
                else:
                    print("something is wrong!")
                    break
                    
                countsold=int(product_site.find("div", {'class', 'psold'}).find("span", {'class', 'pcountsold'}).text.replace(".", ""))
                # Steam the image from the url
                request = requests.get(image_url, stream=True)
            
                # Get the filename from the url, used for saving later
                file_name = str(product.name)+".jpg"
            
                # Create a temporary file
                lf = tempfile.NamedTemporaryFile()
            
                # Read the streamed image in sections
                for block in request.iter_content(1024 * 8):
            
                    # If no more file then stop
                    if not block:
                        break
            
                    # Write image block to temporary file
                    lf.write(block)
          
        
                new_entry=part()
                new_entry.product=product
                new_entry.image.save(file_name, files.File(lf))
                new_entry.description=description
                new_entry.price=price
                new_entry.rating=rating
                new_entry.specs_categorys=specs_categorys
                new_entry.specs_values=specs_values
                new_entry.available_amount=available_amount
                new_entry.available_from=available_from
                new_entry.countsold=countsold
                new_entry.save()
                            
        
    def handle(self, *args, **options):
        self.crawl_product_info()
