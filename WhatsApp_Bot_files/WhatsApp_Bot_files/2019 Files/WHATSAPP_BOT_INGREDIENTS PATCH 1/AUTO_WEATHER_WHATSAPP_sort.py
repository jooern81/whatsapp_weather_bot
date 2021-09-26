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
import pyperclip

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

WeatherIntroMessages = [','+ Ewarn+ ' do take note that the following stations may experience rain in the next 2 hours'+Ewarn+': ',
                        ', expect rain in the following'+ Etrain + 'stations in the next 2 hours: ',
                        ', there is chance of'+ Edrops + 'rain' +Edrops+' affecting the stations stated below: ',
                        ', you may have to get your'+ Epayung + 'out if you are in the following stations during the next 2 hours:',
                        ', Dark' + Ecloud + 'detected, expect rain in the next 2 hours for the stations listed below:']

WeatherOutroMessages = ['Please drive and work safely, your safety is our priority.',
                        'Rainy weather makes the roads more dangerous, think of your family, drive and work safely. ',
                        'Work and drive carefully, all it takes is one accident.' + Ehospital,
                        'Please work and drive carefully, life is valuable. ' + Ecar,
                        'Your life is precious, drive slowly and work carefully.' + Econtractor,
                        'Take the necessary safety precautions and work safely.' + Econtractor,
                        'Casual + Safety = Casualty, your attitude counts, so take safety seriously' +Eokay,
                        'Slip and Falls can lead to serious injury. Even if you are lucky, it still leads to embarrassment' + Esmirk,
                        'Life did not begin by accident. Do not end it by one.' + Erelieve]

def send_msg(recipient, rainzone_msg):
    intro_msg = random.choice(WeatherIntroMessages)
    outro_msg = random.choice(WeatherOutroMessages)
    print(intro_msg + '\n' + rainzone_msg + '\n' + outro_msg)
    time.sleep(10)

    #intro_msg = intro_msg.upper()  # use upper for caps
    #rainzone_msg = rainzone_msg.upper()
    #outro_msg = outro_msg.upper()
    
    # intro
    pyautogui.typewrite(recipient, interval=0.001)
    pyperclip.copy(intro_msg)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('shift','\n')
    # body
    for line in rainzone_msg.split('\n'):
        pyautogui.typewrite(line, interval=0.001)
        pyautogui.hotkey('shift','\n')
    # outro
    pyautogui.hotkey('shift','\n')
    pyperclip.copy(outro_msg)
    pyautogui.hotkey('ctrl', 'v')
    # send
    pyautogui.typewrite('\n', interval=0.001)

    
page = requests.get("https://api.data.gov.sg/v1/environment/2-hour-weather-forecast")
soup=BeautifulSoup(page.content,"html.parser")
goodsoup = soup.prettify()

#Clean up soup
for char in string.punctuation:
    goodsoup = goodsoup.replace(char, '')
    
bestsoup = goodsoup.split('Ang Mo Kio')
forecast = "Ang Mo Kio" + bestsoup[2]
listforecast = forecast.split("area")
listforecast[-1] = listforecast[-1].split("api").pop(0) 

listforecast = [i.split("forecast") for i in listforecast]
    
#Set up Area divisions
listofrain = list()

#create the list of rainy areas
#listofrainzones = []
# Assign Addresses to Areas
NZareas = {'Ang Mo Kio': ['Ang Mo Kio','Yio Chu Kang'],
           'Bishan': ['Bishan', 'Marymount'],
           'Sembawang': ['Sembawang','Canberra'],
           'Sungei Kadut': ['Kranji'],
           'Toa Payoh': ['Braddell','Toa Payoh','Caldecott'],
           'Woodlands': ['Marsiling','Woodlands','Admiralty'],
           'Yishun': ['Khatib']}
CENTRALareas = {'Bukit Merah': ['Outram Park','Tiong Bahru','Redhill','Labrador Park','Telok Blangah','Harbourfront'],
                'Bukit Timah': ['Holland Village'],
                'City': ['Dhoby Ghaut','City Hall','Raffles Place','Bugis','Tanjong Pagar','Bras Basah','Esplanade','Promenade','Nicoll Highway','Marina Bay','Marina South Pier'],
                'Kallang': ['Kallang','Lavendar','Stadium','Mountbatten'],
                'Novena': ['Novena','Newton','Orchard','Somerset'],
                'Queenstown': ['Queenstown','Commonwealth','Buona Vista','Dover','One North','Kent Ridge','Haw Par Villa','Pasir Panjang'],
                'Tanglin': ['Botanic Gardens','Farrer Road']}
EZareas = {'Bedok': ['Tanah Merah','Bedok','Kembangan'],
           'Changi': ['Changi'],
           'Geylang': ['Eunos','Paya Lebar','Aljunied','Dakota','Macpherson'],
           'Hougang': ['Pasir Ris'],
           'Tampines': ['Tampines','Simei','Expo'],
           'Serangoon': ['Bartley','Serangoon','Lorong Chuan']}
#SZareas = ['Marine Parade', 'City', 'Bukit Merah', 'Clementi', 'Queenstown']
WZareas = {'Bukit Batok': ['Bukit Batok','Bukit Gombak'],
           'Choa Chu Kang': ['Choa Chu Kang','Yew Tee'],
           'Clementi': ['Clementi'],
           'Jurong East': ['Lakeside','Boon Lay','Pioneer','Jurong East','Chinese Garden'],
           'Pioneer':['Joo Koon','Gul Circle'],
           'Tuas': ['Tuas Cresent','Tuas West Road','Tuas Link']}

MRT_Stations = ['']
# Determine Rain Areas
for fc in listforecast:
    if "Shower" in fc[1] or "Rain" in fc[1]:
        listofrain.append(fc)
print(datetime.datetime.now().strftime('%H%M'))
print(listofrain)

rainzone_msg = ''
#station_name = ''
nz = []
cl = []
ez = []
wz = []
for rn in listofrain:
    key = rn[0]
    if key in NZareas:
        nz.extend(NZareas[key])
    elif key in CENTRALareas:
        cl.extend(CENTRALareas[key])
    elif key in EZareas:
        ez.extend(EZareas[key])
    elif key in WZareas:
        wz.extend(WZareas[key])
if nz != []:
    nz.insert(0,'\n*North Zone:*')
if cl != []:
    cl.insert(0,'\n*Central:*')
if ez != []:
    ez.insert(0,'\n*East Zone:*')
if wz != []:
    wz.insert(0,'\n*West Zone:*')

nz.sort()
cl.sort()
ez.sort()
wz.sort()

rainzone_msg = '\n'.join(nz+cl+ez+wz) + '\n'

"""
#for i in range(len(listofrain)):
#    if listofrain[i][0] in NZareas:
#        if 'Northen Region' not in listofrainzones:
#            rainzone_msg = rainzone_msg + '\nNorthern Region: \n'
#            listofrainzones.append('Northern Region')
#        station_name = listofrain[i][0] + ' MRT station\n'
#        rainzone_msg = rainzone_msg + station_name

header = 0
for rn in listofrain:
    for key in NZareas:
        if rn[0] == key:
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
for rn in listofrain:
    for key in CENTRALareas:
        if rn[0] == key:
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
for rn in listofrain:
    for key in EZareas:
        if rn[0] == key:
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
"""
            
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
if (datetime.datetime.now().strftime('%H%M')) > '0730' and (datetime.datetime.now().strftime('%H%M')) < '2130' and nz != [] and ez != [] and cl != [] and wz != []:
    recipient = "Team LMZ"    
    send_msg(recipient, rainzone_msg)
    
elif (datetime.datetime.now().strftime('%H%M')) > '0030' and (datetime.datetime.now().strftime('%H%M')) < '0430' and nz != [] and ez != [] and cl != [] and wz != []:
    recipient = "Good evening LMZ"
    send_msg(recipient, rainzone_msg)

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
if (datetime.datetime.now().strftime('%H%M')) > '0730' and (datetime.datetime.now().strftime('%H%M')) < '2130' and nz != [] and ez != [] and cl != [] and wz != []:
    recipient = "Hello ERU"
    send_msg(recipient, rainzone_msg)
    
    
elif (datetime.datetime.now().strftime('%H%M')) > '0030' and (datetime.datetime.now().strftime('%H%M')) < '0430' and nz != [] and ez != [] and cl != [] and wz != []:
    recipient = "Attention all Maintenance Teams"
    send_msg(recipient, rainzone_msg)

    
if nz != [] and ez != [] and cl != [] and wz != [] and WhatsApp_Message != "":
    time.sleep(10800)
    
