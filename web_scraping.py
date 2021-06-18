# -*- coding: utf-8 -*-
"""
Created on Mon May  3 21:28:12 2021

@author: Karnas
"""


import requests
from bs4 import BeautifulSoup as bs
github_user=input("Input User name:")
url='https://github.com/'+github_user
r=requests.get(url)
soup=bs(r.content,'html.parser')
profile_image=soup.find('img',{'alt':'Avatar'})['src']
print(profile_image)