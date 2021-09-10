# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:46:00 2020

@author: CoilingSnake
"""
import pandas as pd
import requests
import time
from bs4 import BeautifulSoup
import pandas as pd

'''

url = 'https://www.ebay.com/itm/Metallica-Master-Of-Puppets-New-Vinyl-LP-Rmst/132394413453?_trkparms=aid%3D1110006%26algo%3DHOMESPLICE.SIM%26ao%3D1%26asc%3D226053%26meid%3Df9a20517dc8a4220822189492af109ff%26pid%3D100005%26rk%3D5%26rkt%3D12%26mehot%3Dpf%26sd%3D292995223490%26itm%3D132394413453%26pmt%3D1%26noa%3D0%26pg%3D2047675%26algv%3DSimplAMLv5PairwiseWebWithBBEV1Filter&_trksid=p2047675.c100005.m1851'


headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
        'referrer': 'google.com',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Pragma': 'no-cache',
        }

jar = requests.cookies.RequestsCookieJar()
jar.set('dp1','bkms/in61c0e811^u1f/Alyssa61c0e811^tzo/-785dfe8f21^pcid/19434569215fdfb491^u1p/eGlhbmZyYXRlXzcz61c0e811^bl/USen-US61c0e811^expt/00015627750338225e16a7b9^pbf/%232004440e400e0001081a8c20000045fdfb491^')

session = requests.Session()
session.cookies = jar

response = session.get(url , headers=headers, timeout = 10) #timeout is 8 seck

soup = BeautifulSoup(response.text, 'html.parser')

category_list = soup.find_all("li", attrs={'itemprop':'itemListElement'})

category = []
for each in category_list:
    category = category + [each.text,]
category = ','.join(category)

if 'Clothing' in category or 'Shoes' in category or 'Books' in category or 'DVD' in category or 'Records' in category:
    print('\nCategory contains unwanted items: ')
    print(category.replace('\n',''))
    
    
'''
file_folder = ''
end_file_name = file_folder+"ID outs.csv"

data_frame = pd.read_csv(end_file_name , engine='python').drop_duplicates(subset='Store', keep='first', inplace=False)
data_frame.to_csv(file_folder+'ID outs_nonDuplicate.csv', index=False , encoding = 'utf-8')