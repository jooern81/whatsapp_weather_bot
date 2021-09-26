# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:25:32 2019

@author: chinjooern
"""
import random
import requests
import string
import datetime
import pyautogui
import time
import cv2

from pyscreeze import ImageNotFoundException
from bs4 import BeautifulSoup


page = requests.get("https://api.data.gov.sg/v1/environment/2-hour-weather-forecast")
soup=BeautifulSoup(page.content,"html.parser")
goodsoup = soup.prettify()

#Clean up soup
for char in string.punctuation:
    goodsoup = goodsoup.replace(char, '')
    
bestsoup = goodsoup.split('Ang Mo Kio')
forecast = "Ang Mo Kio" + bestsoup[2]
listforecast = forecast.split("area")
listforecast[len(listforecast)-1] = listforecast[len(listforecast)-1].split("api").pop(0) 

for i in range(len(listforecast)):
    listforecast[i] = listforecast[i].split("forecast")
    
#Set up Area divisions
listofrain = []             #create the list of rainy areas
listofrainzones = []

#Assign Addresses to Areas
NZareas = ['Sembawang','Woodlands', 'Mandai', 'Yishun', 'Lim Chu Kang', 'Sungei Kadut', 'Seletar', 'Punggol', 'Sengkang','Seletar']
CENTRALareas = ['Serangoon', 'Novena', 'Central Water Catchment', 'Ang Mo Kio', 'Toa Payoh', 'Bukit Timah', 'Bukit Panjang', 'Bishan']
EZareas = ['Pasir Ris', 'Tampines', 'Changi', 'Bedok', 'Paya Lebar', 'Geylang','Kallang', 'Hougang', 'Marine Parade']
SZareas = ['Marine Parade', 'City', 'Bukit Merah', 'Clementi', 'Queenstown' ]
WZareas = ['Tuas', 'Pioneer', 'Boon Lay', 'Bukit Batok', 'Choa Chu Kang', 'Clementi', 'Jalan Bahar', 'Western Water Catchment', 'Tengah', 'Bukit Batok', 'Jurong West', 'Jurong East']

#Determine Rain Areas
print(listforecast)
for i in range(len(listforecast)):          
    if ("Shower" or "Rain") in listforecast[i][1]:
        print(listforecast[i])
        listofrain.append(listforecast[i])

print(listofrain)

for i in range(len(listofrain)):
    if listofrain[i][0] in NZareas:
        if 'Northern Region' not in listofrainzones:
            listofrainzones.append('Northern Region')
        
for i in range(len(listofrain)):
    if listofrain[i][0] in CENTRALareas:
        if 'Central Region' not in listofrainzones:
            listofrainzones.append('Central Region')
        
for i in range(len(listofrain)):
    if listofrain[i][0] in EZareas:
        if 'Eastern Region' not in listofrainzones:
            listofrainzones.append('Eastern Region')
            
for i in range(len(listofrain)):
    if listofrain[i][0] in SZareas:
        if 'Southern Region' not in listofrainzones:
            listofrainzones.append('Southern Region')
    
for i in range(len(listofrain)):
    if listofrain[i][0] in WZareas:
        if 'Western Region' not in listofrainzones:
            listofrainzones.append('Western Region')
            
#Find WhatsApp Group 1
try:
     (image_x, image_y) = pyautogui.locateCenterOnScreen(r"C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS\TOHWEIQI.png", grayscale=True, confidence=.5)       # returns (left, top, width, height) of first place it is found
     print("WHATSAPP GROUP 1 FOUND")
except ImageNotFoundException:
    (image_x, image_y) = pyautogui.locateCenterOnScreen(r"C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS\TOHWEIQI_CLICKED.png", grayscale=True, confidence=.5)
    print("WHATSAPP GROUP 1 FOUND")

#Click on WhatsApp Group 1
pyautogui.click(x=image_x, y=image_y, clicks=1, button='left')

#Check time before sending message
if (datetime.datetime.now().strftime('%H%M')) > '0730' and (datetime.datetime.now().strftime('%H%M')) < '2130' and (listofrainzones) != []:
    recipient = "Team LMZ"
    WeatherIntroMessages = [recipient + ', do take note that the following regions may experience rain in the next 2 hours: ', recipient + ', expect rain in the following regions in the next 2 hours: ']
    WeatherOutroMessages = [' Please drive and work safely, your safety is our priority.',' Rainy weather makes the roads more dangerous, think of your family, drive and work safely. ',' Work and drive carefully, all it takes is one accident.',' Please work and drive carefully, life is valuable. ',' Your life is precious, drive slowly and work carefully.']    
    WhatsApp_Message = (WeatherIntroMessages[random.randint(0,len(WeatherIntroMessages)-1)] + str(listofrainzones) + WeatherOutroMessages[random.randint(0,len(WeatherOutroMessages)-1)]) 
    print(WhatsApp_Message)
    time.sleep(10)
    pyautogui.typewrite(WhatsApp_Message +'\n', interval=0.001)
    
if (datetime.datetime.now().strftime('%H%M')) > '0030' and (datetime.datetime.now().strftime('%H%M')) < '0430' and (listofrainzones) != []:
    recipient = "Good evening LMZ"
    WeatherIntroMessages = [recipient + ', do take note that the following regions may experience rain in the next 2 hours: ', recipient + ', expect rain in the following regions in the next 2 hours: ']
    WeatherOutroMessages = [' Please drive safely, and seek shelter at the nearest station if necessary, your safety is our priority.',' Rainy weather makes work more dangerous, do confirm weather conditions at your sector before working. ',' Do confirm weather conditions at your sector before beginning work. Work safely, all it takes is one accident.',' Please confirm weather conditions at your sector before working, life is valuable. ',' Your life is precious, please confirm weather conditions at your sector before working.'] 
    WhatsApp_Message = (WeatherIntroMessages[random.randint(0,len(WeatherIntroMessages)-1)] + str(listofrainzones) + WeatherOutroMessages[random.randint(0,len(WeatherOutroMessages)-1)]) 
    print(WhatsApp_Message)
    time.sleep(10)
    pyautogui.typewrite(WhatsApp_Message +'\n', interval=0.001)

#Find WhatsApp Group 2
try:
     (image_x, image_y) = pyautogui.locateCenterOnScreen(r"C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS\ERUMOC.png", grayscale=True, confidence=.5)       # returns (left, top, width, height) of first place it is found
     print("WHATSAPP GROUP 2 FOUND")
except ImageNotFoundException:
    (image_x, image_y) = pyautogui.locateCenterOnScreen(r"C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS\ERUMOC_CLICKED.png", grayscale=True, confidence=.5)
    print("WHATSAPP GROUP 2 FOUND")

#Click on WhatsApp Group 2
pyautogui.click(x=image_x, y=image_y, clicks=1, button='left')

#Check time before sending message
if (datetime.datetime.now().strftime('%H%M')) > '0730' and (datetime.datetime.now().strftime('%H%M')) < '2130' and (listofrainzones) != []:
    recipient = "Hello ERU"
    WeatherIntroMessages = [recipient + ', do take note that the following regions may experience rain in the next 2 hours: ', recipient + ', expect rain in the following regions in the next 2 hours: ']
    WeatherOutroMessages = [' Please drive and work safely, your safety is our priority.',' Rainy weather makes the roads more dangerous, think of your family, drive and work safely. ',' Work and drive carefully, all it takes is one accident.',' Please work and drive carefully, life is valuable. ',' Your life is precious, drive slowly and work carefully.']    
    WhatsApp_Message = (WeatherIntroMessages[random.randint(0,len(WeatherIntroMessages)-1)] + str(listofrainzones) + WeatherOutroMessages[random.randint(0,len(WeatherOutroMessages)-1)]) 
    print(WhatsApp_Message)
    time.sleep(10)
    pyautogui.typewrite(WhatsApp_Message +'\n', interval=0.001)
    
    
if (datetime.datetime.now().strftime('%H%M')) > '0030' and (datetime.datetime.now().strftime('%H%M')) < '0430' and (listofrainzones) != []:
    recipient = "Attention all Maintenance Teams"
    WeatherIntroMessages = [recipient + ', do take note that the following regions may experience rain in the next 2 hours: ', recipient + ', expect rain in the following regions in the next 2 hours: ']
    WeatherOutroMessages = [' Please drive safely, and seek shelter at the nearest station if necessary, your safety is our priority.',' Rainy weather makes work more dangerous, do confirm weather conditions at your sector before working. ',' Do confirm weather conditions at your sector before beginning work. Work safely, all it takes is one accident.',' Please confirm weather conditions at your sector before working, life is valuable. ',' Your life is precious, please confirm weather conditions at your sector before working.']    
    WhatsApp_Message = (WeatherIntroMessages[random.randint(0,len(WeatherIntroMessages)-1)] + str(listofrainzones) + WeatherOutroMessages[random.randint(0,len(WeatherOutroMessages)-1)]) 
    print(WhatsApp_Message)
    time.sleep(10)
    pyautogui.typewrite(WhatsApp_Message +'\n', interval=0.001)

if (listofrainzones) != [] and WhatsApp_Message != "":
    time.sleep(10800)
    
