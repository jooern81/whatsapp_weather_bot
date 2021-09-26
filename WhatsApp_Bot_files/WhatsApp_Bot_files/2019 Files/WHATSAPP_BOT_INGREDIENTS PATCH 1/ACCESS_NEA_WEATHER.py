# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 17:01:48 2019

@author: chinjooern
"""

import requests
import string
page = requests.get("https://api.data.gov.sg/v1/environment/2-hour-weather-forecast")

from bs4 import BeautifulSoup
soup=BeautifulSoup(page.content,"html.parser")
goodsoup = soup.prettify()

for char in string.punctuation:
    goodsoup = goodsoup.replace(char, '')
    
goodsoup.split("Ang Mo Kio")
len(goodsoup.split("Ang Mo Kio"))

forecast = "Ang Mo Kio" + (goodsoup.split("Ang Mo Kio"))[2]
listforecast = forecast.split("area")


for i in range(len(listforecast)):
    listforecast[i] = listforecast[i].split("forecast")
    print(listforecast[i])
   
    
