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
from pyscreeze import ImageNotFoundException
from bs4 import BeautifulSoup

while True:
    
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
    
    #Find WhatsApp Group
    try:
         (image_x, image_y) = pyautogui.locateCenterOnScreen('TOHWEIQI.png')       # returns (left, top, width, height) of first place it is found
         print("WHATSAPP GROUP FOUND")
    except ImageNotFoundException:
        (image_x, image_y) = pyautogui.locateCenterOnScreen('TOHWEIQI_CLICKED.png')
        print("WHATSAPP GROUP FOUND")
    
    #Click on WhatsApp Group
    pyautogui.click(x=image_x, y=image_y, clicks=1, button='left')
    
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
            if 'Northen Region' not in listofrainzones:
                listofrainzones.append('Northen Region')
            
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
    
    #Message Customization
    recipient = "Team LMZ"
    WeatherIntroMessages = [recipient + ', do take note that the following regions may experience rain in the next 2 hours: ', recipient + ', expect rain in the following regions in the next 2 hours: ']
    WeatherOutroMessages = [' Please drive safely, your safety is our priority.',' Rainy weather makes the roads more dangerous, think of your family, drive safely. ',' Drive carefully, all it takes is one accident.',' Drive slowly and carefully, life is valuable. ',' Your life is precious, drive slowly and carefully.']
            
    WhatsApp_Message = (WeatherIntroMessages[random.randint(0,len(WeatherIntroMessages)-1)] + str(listofrainzones) + WeatherOutroMessages[random.randint(0,len(WeatherOutroMessages)-1)])     
    
    
    
    #Check time before sending message
    if (datetime.datetime.now().strftime('%H%M')) > '0730' and (datetime.datetime.now().strftime('%H%M')) < '2230' and (listofrainzones) != []:
        print(WhatsApp_Message)
        pyautogui.typewrite(WhatsApp_Message +'\n', interval=0.001)
        
    time.sleep(1000)