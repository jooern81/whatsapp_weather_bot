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
import emoji

from pyscreeze import ImageNotFoundException
from bs4 import BeautifulSoup

#Import emojis
Eokay = emoji.emojize(':ok_hand:', use_aliases = True)
Epayung = emoji.emojize(' :umbrella: ', use_aliases = True)
Esmirk = emoji.emojize(' :smirk: ', use_aliases = True)
Evee = emoji.emojize(' :v: ', use_aliases = True)
Econtractor = emoji.emojize(' :construction_worker: ', use_aliases = True)
Etroll = emoji.emojize(' :trollface: ', use_aliases = True)
Ehospital = emoji.emojize(' :hospital: ', use_aliases = True)
Erelieve = emoji.emojize(' :relieved: ', use_aliases = True)
Ecloud = emoji.emojize(' :cloud: ', use_aliases = True)
Edrops = emoji.emojize(' :sweat_drops: ', use_aliases = True)
Ecar = emoji.emojize(' :car: ', use_aliases = True)
Ewarn = emoji.emojize(' :warning: ', use_aliases = True)
Etrain = emoji.emojize(' :light_rail: ', use_aliases = True)

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

# Assign Addresses to Areas
NZareas = {'Ang Mo Kio': 'Ang Mo Kio\nYio Chu Kang\n', 'Bishan': 'Bishan\nMarymount\n', 'Sembawang': 'Sembawang\nCanberra\n',
           'Sungei Kadut':'Kranji', 'Toa Payoh':'Braddell\nToa Payoh\nCaldecott\n',
            'Woodlands': 'Marsiling\nWoodlands\nAdmiralty\n', 'Yishun': 'Khatib\n'}
CENTRALareas = {'Bukit Merah': 'Outram Park\nTiong Bahru\nRedhill\nLabrador Park\nTelok Blangah\nHarbourfront\n',
                'Bukit Timah': 'Holland Village\n',
                'City': 'Dhoby Ghaut\nCity Hall\nRaffles Place\nBugis\nTanjong Pagar\nBras Basah\nEsplanade\nPromenade\nNicoll Highway\nMarina Bay\n Marina South Pier\n',
                'Kallang': 'Kallang\nLavendar\nStadium\nMountbatten\n', 'Novena': 'Novena\nNewton\nOrchard\nSomerset\n',
                'Queenstown': 'Queenstown\nCommonwealth\nBuona Vista\nDover\nOne North\nKent Ridge\nHaw Par Villa\nPasir Panjang\n', 'Tanglin': 'Botanic Gardens\nFarrer Road\n'}
EZareas = {'Bedok': 'Tanah Merah\nBedok\nKembangan\n', 'Changi': 'Changi\n',
            'Geylang': 'Eunos\nPaya Lebar\nAljunied\nDakota\nMacpherson\n', 'Hougang': 'Pasir Ris\n',
            'Tampines': 'Tampines\nSimei\nExpo', 'Serangoon': 'Bartley\nSerangoon\nLorong Chuan\n'}
SZareas = ['Marine Parade', 'City', 'Bukit Merah', 'Clementi', 'Queenstown']
WZareas = {'Bukit Batok': 'Bukit Batok\nBukit Gombak\n', 'Choa Chu Kang': 'Choa Chu Kang\nYew Tee\n',
            'Clementi': 'Clementi\n', 'Jurong East': 'Lakeside\nBoonLay\nPioneer\n', 'Pioneer':'Joo Koon\nGul Circle\n',
            'Tuas': 'Tuas Cresent\nTuas West Road\nTuas Link\n'}

MRT_Stations = ['']
# Determine Rain Areas
for i in range(len(listforecast)):
    if "Cloudy" in listforecast[i][1] or "Rain" in listforecast[i][1]:
        listofrain.append(listforecast[i])
        print(listofrain)

rainzone_msg = ''
station_name = ''
#for i in range(len(listofrain)):
#    if listofrain[i][0] in NZareas:
#        if 'Northen Region' not in listofrainzones:
#            rainzone_msg = rainzone_msg + '\nNorthern Region: \n'
#            listofrainzones.append('Northern Region')
#        station_name = listofrain[i][0] + ' MRT station\n'
#        rainzone_msg = rainzone_msg + station_name
header = 0
for i in range(len(listofrain)):
    for key in NZareas:
        if listofrain[i][0] == key:
            if header == 0:
                rainzone_msg = rainzone_msg + '*Northen Zone:*\n'
                header = 1
            rainzone_msg = rainzone_msg + NZareas[key]
header = 1
#for i in range(len(listofrain)):
#    if listofrain[i][0] in CENTRALareas:
#        if 'Central Region' not in listofrainzones:
#            rainzone_msg = rainzone_msg + '\nCentral Region: \n'
#            listofrainzones.append('Central Region')
#        station_name = listofrain[i][0] + ' MRT station\n'
#        rainzone_msg = rainzone_msg + station_name
header = 0
for i in range(len(listofrain)):
    for key in CENTRALareas:
        if listofrain[i][0] == key:
            if header == 0:
                rainzone_msg = rainzone_msg + '*Central Zone:*\n'
                header = 1
            rainzone_msg = rainzone_msg + CENTRALareas[key]
header = 1
#for i in range(len(listofrain)):
#    if listofrain[i][0] in EZareas:
#        if 'Eastern Region' not in listofrainzones:
#            rainzone_msg = rainzone_msg + '\nEastern Region: \n'
#            listofrainzones.append('Eastern Region')
#        station_name = listofrain[i][0] + ' MRT station \n'
#        rainzone_msg = rainzone_msg + station_name
header = 0
for i in range(len(listofrain)):
    for key in EZareas:
        if listofrain[i][0] == key:
            if header == 0:
                rainzone_msg = rainzone_msg + '*Eastern Zone:*\n'
                header = 1
            rainzone_msg = rainzone_msg + EZareas[key]
header = 1
#for i in range(len(listofrain)):
#    if listofrain[i][0] in SZareas:
#        if 'Southern Region' not in listofrainzones:
#            rainzone_msg = rainzone_msg + '\nSouthern Region: \n'
#            listofrainzones.append('Southern Region')
#        station_name = listofrain[i][0] + ' MRT station \n'
#        rainzone_msg = rainzone_msg + station_name

#for i in range(len(listofrain)):
#    if listofrain[i][0] in WZareas:
#        if 'Western Region' not in listofrainzones:
#            rainzone_msg = rainzone_msg + '\nWestern Region: \n'
#            listofrainzones.append('Western Region')
#        station_name = listofrain[i][0] + ' MRT station \n'
#        rainzone_msg = rainzone_msg + station_name
header = 0
for i in range(len(listofrain)):
    for key in WZareas:
        if listofrain[i][0] == key:
            if header == 0:
                rainzone_msg = rainzone_msg + '*Western Zone:*\n'
                header = 1
            rainzone_msg = rainzone_msg + WZareas[key]
header = 1

            
#Find WhatsApp Group 1
try:
     (image_x, image_y) = pyautogui.locateCenterOnScreen(r"C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS PATCH 1\TOHWEIQI.png", grayscale=True, confidence=.5)       # returns (left, top, width, height) of first place it is found
     print("WHATSAPP GROUP 1 FOUND")
except ImageNotFoundException:
    (image_x, image_y) = pyautogui.locateCenterOnScreen(r"C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS PATCH 1\TOHWEIQI_CLICKED.png", grayscale=True, confidence=.5)
    print("WHATSAPP GROUP 1 FOUND")

#Click on WhatsApp Group 1
pyautogui.click(x=image_x, y=image_y, clicks=1, button='left')

#Check time before sending message
if (datetime.datetime.now().strftime('%H%M')) > '0730' and (datetime.datetime.now().strftime('%H%M')) < '2130' and (listofrain) != []:
    recipient = "Team LMZ"
    WeatherIntroMessages = [recipient + ','+ Ewarn+ ' do take note that the following stations may experience rain in the next 2 hours'+Ewarn+': \n',recipient + ', expect rain in the following'+ Etrain + 'stations in the next 2 hours: \n',recipient + ', there is chance of'+ Edrops + 'rain' +Edrops+' affecting the stations stated below: \n',recipient + ', you may have to get your'+ Epayung + 'out if you are in the following stations for the next 2 hours:\n',recipient + ', Dark' + Ecloud + 'detected, expect rain in the next 2 hours for the stations listed below\n']
    WeatherOutroMessages = [' \nPlease drive and work safely, your safety is our priority.',' \nRainy weather makes the roads more dangerous, think of your family, drive and work safely. ',' \nWork and drive carefully, all it takes is one accident.' + Ehospital,' \nPlease work and drive carefully, life is valuable. ' + Ecar,' \nYour life is precious, drive slowly and work carefully.' + Econtractor,' \nTake the necessary safety precautions and work safely.' + Econtractor,' \nCasual + Safety = Casualty, your attitude counts, so take safety seriously' +Eokay,' \nSlip and Falls can lead to serious injury, otherwise it can be pretty emberassing' + Esmirk,' \nLife did not begin by accident. Do not end it as one.' + Erelieve]
    WhatsApp_Message = (WeatherIntroMessages[random.randint(0, len(WeatherIntroMessages) - 1)] + rainzone_msg + WeatherOutroMessages[random.randint(0, len(WeatherOutroMessages) - 1)])
    print(WhatsApp_Message)
    time.sleep(10)
    pyautogui.typewrite(WhatsApp_Message +'\n', interval=0.001)
    
if (datetime.datetime.now().strftime('%H%M')) > '2310' and (datetime.datetime.now().strftime('%H%M')) < '2430' and (listofrain) != []:
    recipient = "Good evening LMZ"
    WeatherIntroMessages = [recipient + ','+ Ewarn+ ' do take note that the following stations may experience rain in the next 2 hours'+Ewarn+': \n',recipient + ', expect rain in the following'+ Etrain + 'stations in the next 2 hours: \n',recipient + ', there is chance of'+ Edrops + 'rain' +Edrops+' affecting the stations stated below: \n',recipient + ', you may have to get your'+ Epayung + 'out if you are in the following stations for the next 2 hours:\n',recipient + ', Dark' + Ecloud + 'detected, expect rain in the next 2 hours for the stations listed below\n']
    WeatherOutroMessages = [' \nPlease drive and work safely, your safety is our priority.',' \nRainy weather makes the roads more dangerous, think of your family, drive and work safely. ',' \nWork and drive carefully, all it takes is one accident.' + Ehospital,' \nPlease work and drive carefully, life is valuable. ' + Ecar,' \nYour life is precious, drive slowly and work carefully.' + Econtractor,' \nTake the necessary safety precautions and work safely.' + Econtractor,' \nCasual + Safety = Casualty, your attitude counts, so take safety seriously' +Eokay,' \nSlip and Falls can lead to serious injury, otherwise it can be pretty emberassing' + Esmirk,' \nLife did not begin by accident. Do not end it as one.' + Erelieve]
    WhatsApp_Message = (WeatherIntroMessages[random.randint(0, len(WeatherIntroMessages) - 1)] + rainzone_msg + WeatherOutroMessages[random.randint(0, len(WeatherOutroMessages) - 1)])
    print(WhatsApp_Message)
    time.sleep(10)
    pyautogui.keyDown('shift')
    pyautogui.press('capslock')
    pyautogui.typewrite(WhatsApp_Message +'\n', interval=0.001)
    pyautogui.press('capslock')
    pyautogui.keyUp('shift')

#Find WhatsApp Group 2
try:
     (image_x, image_y) = pyautogui.locateCenterOnScreen(r"C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS PATCH 1\ERUMOC.png", grayscale=True, confidence=.5)       # returns (left, top, width, height) of first place it is found
     print("WHATSAPP GROUP 2 FOUND")
except ImageNotFoundException:
    (image_x, image_y) = pyautogui.locateCenterOnScreen(r"C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS PATCH 1\ERUMOC_CLICKED.png", grayscale=True, confidence=.5)
    print("WHATSAPP GROUP 2 FOUND")

#Click on WhatsApp Group 2
pyautogui.click(x=image_x, y=image_y, clicks=1, button='left')

#Check time before sending message
if (datetime.datetime.now().strftime('%H%M')) > '0730' and (datetime.datetime.now().strftime('%H%M')) < '2130' and (listofrain) != []:
    recipient = "Hello ERU"
    WeatherIntroMessages = [recipient + ','+ Ewarn+ ' do take note that the following stations may experience rain in the next 2 hours'+Ewarn+': \n',recipient + ', expect rain in the following'+ Etrain + 'stations in the next 2 hours: \n',recipient + ', there is chance of'+ Edrops + 'rain' +Edrops+' affecting the stations stated below: \n',recipient + ', you may have to get your'+ Epayung + 'out if you are in the following stations for the next 2 hours:\n',recipient + ', Dark' + Ecloud + 'detected, expect rain in the next 2 hours for the stations listed below\n']
    WeatherOutroMessages = [' \nPlease drive and work safely, your safety is our priority.',' \nRainy weather makes the roads more dangerous, think of your family, drive and work safely. ',' \nWork and drive carefully, all it takes is one accident.' + Ehospital,' \nPlease work and drive carefully, life is valuable. ' + Ecar,' \nYour life is precious, drive slowly and work carefully.' + Econtractor,' \nTake the necessary safety precautions and work safely.' + Econtractor,' \nCasual + Safety = Casualty, your attitude counts, so take safety seriously' +Eokay,' \nSlip and Falls can lead to serious injury, otherwise it can be pretty emberassing' + Esmirk,' \nLife did not begin by accident. Do not end it as one.' + Erelieve]
    WhatsApp_Message = (WeatherIntroMessages[random.randint(0, len(WeatherIntroMessages) - 1)] + rainzone_msg + WeatherOutroMessages[random.randint(0, len(WeatherOutroMessages) - 1)])
    print(WhatsApp_Message)
    time.sleep(10)
    pyautogui.typewrite(WhatsApp_Message +'\n', interval=0.001)
    
    
if (datetime.datetime.now().strftime('%H%M')) > '0030' and (datetime.datetime.now().strftime('%H%M')) < '0430' and (listofrain) != []:
    recipient = "Attention all Maintenance Teams"
    WeatherIntroMessages = [recipient + ','+ Ewarn+ ' do take note that the following stations may experience rain in the next 2 hours'+Ewarn+': \n',recipient + ', expect rain in the following'+ Etrain + 'stations in the next 2 hours: \n',recipient + ', there is chance of'+ Edrops + 'rain' +Edrops+' affecting the stations stated below: \n',recipient + ', you may have to get your'+ Epayung + 'out if you are in the following stations for the next 2 hours:\n',recipient + ', Dark' + Ecloud + 'detected, expect rain in the next 2 hours for the stations listed below\n']
    WeatherOutroMessages = [' \nPlease drive and work safely, your safety is our priority.',' \nRainy weather makes the roads more dangerous, think of your family, drive and work safely. ',' \nWork and drive carefully, all it takes is one accident.' + Ehospital,' \nPlease work and drive carefully, life is valuable. ' + Ecar,' \nYour life is precious, drive slowly and work carefully.' + Econtractor,' \nTake the necessary safety precautions and work safely.' + Econtractor, ' \nCasual + Safety = Casualty, your attitude counts, so take safety seriously' +Eokay,' \nSlip and Falls can lead to serious injury, otherwise it can be pretty emberassing' + Esmirk,' \nLife did not begin by accident. Do not end it as one.' + Erelieve]
    WhatsApp_Message = (WeatherIntroMessages[random.randint(0, len(WeatherIntroMessages) - 1)] + rainzone_msg + WeatherOutroMessages[random.randint(0, len(WeatherOutroMessages) - 1)])
    print(WhatsApp_Message)
    time.sleep(10)
    pyautogui.typewrite(WhatsApp_Message +'\n', interval=0.001)

if (listofrainzones) != [] and WhatsApp_Message != "":
    time.sleep(10800)
    
