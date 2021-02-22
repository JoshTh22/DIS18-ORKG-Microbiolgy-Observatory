# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 14:10:51 2021

@author: joshu
"""
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import pandas as pd

url = "https://flexikon.doccheck.com/de/Klinisch_relevante_Bakterien"

page = urlopen(url)

liste = []

html_parser = bs(page, 'html.parser')

content = html_parser.find('div', {"class": "mw-content-ltr"})

names = ''

for i in content.findAll('li'):
    names = i.text.split('\n\n')
    liste.append(names)

flat_list = [item for sublist in liste for item in sublist]

flat_list2 = []

for i in flat_list:
    if i != '\n':
        flat_list2.append(i.strip('\n'))


    
print(flat_list2)


df = pd.DataFrame(flat_list2, columns = ['bacteria'])


df.drop_duplicates().to_csv('bacteria_names.csv', index = False)

#print(liste)
#with open('bacteria_names.csv', 'w') as file:
#    file.write(liste)

