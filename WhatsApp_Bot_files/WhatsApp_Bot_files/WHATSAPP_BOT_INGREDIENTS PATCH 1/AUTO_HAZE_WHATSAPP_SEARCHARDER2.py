# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 17:42:11 2019

@author: joo
"""

import random
import requests
import string
import datetime
import pyautogui
import pyperclip
import re

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
Efamily = emoji.emojize(' :family: ', use_aliases = True)
Emuscle = emoji.emojize(' :muscle: ', use_aliases = True)
Esmoke = emoji.emojize(' :smoking: ', use_aliases = True)


WeatherIntroMessages = ','+ Esmoke + "The 24-hr PSI & PM2.5 readings indicate unhealthy air conditions in the following regions" + Esmoke + ":"
WeatherOutroMessages = 'Employees with chronic lung disease, heart disease, or stroke are also more susceptible to the effects of haze. When the health advisory level follows a 24-hour PSI exceeding 100, these susceptible employees should avoid all outdoor work. If outdoor work is unavoidable, they must use a suitable respirator. For more information: https://www.mom.gov.sg/haze'

def send_msg(recipient, hazezone_msg):
    intro_msg = WeatherIntroMessages
    outro_msg = WeatherOutroMessages
    print(intro_msg + hazezone_msg + outro_msg)
    time.sleep(10)

    #intro_msg = intro_msg.upper()  # use upper for caps
    #rainzone_msg = rainzone_msg.upper()
    #outro_msg = outro_msg.upper()
    
    # intro
    pyautogui.typewrite(recipient, interval=0.001)
    pyperclip.copy(intro_msg)
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('shift','\n')
    pyautogui.hotkey('shift','\n')
    # body
    for line in hazezone_msg.split('\n'):
        pyautogui.typewrite(line, interval=0.001)
        pyautogui.hotkey('shift','\n')
    # outro
    pyperclip.copy(outro_msg)
    pyautogui.hotkey('ctrl', 'v')
    # send
    pyautogui.typewrite('\n', interval=0.001)

    
page2 = requests.get("https://api.data.gov.sg/v1/environment/psi")
soup2=BeautifulSoup(page2.content,"html.parser")
goodsoup2 = soup2.prettify()

goodsoup2 = goodsoup2.split("readings")[1]
goodsoup2 = goodsoup2.split(",")

count = 0
for i in goodsoup2:
    print (count,i)
    count +=1
    

goodsoup2[24] = goodsoup2[24].split('{')[1]
goodsoup2[60] = goodsoup2[60].split('{')[1]
psi = [goodsoup2[54],goodsoup2[55],goodsoup2[56],goodsoup2[57],goodsoup2[58],goodsoup2[59]]

PM25_WEST = goodsoup2[24]
PM25_EAST = goodsoup2[26]
PM25_CENTRAL = goodsoup2[27]
PM25_SOUTH = goodsoup2[28]
PM25_NORTH = goodsoup2[29]

for char in string.punctuation:
    PM25_WEST = PM25_WEST.replace(char, '')
for char in string.ascii_lowercase:
    PM25_WEST = PM25_WEST.replace(char, '')

for char in string.punctuation:
    PM25_EAST = PM25_EAST.replace(char, '')
for char in string.ascii_lowercase:
    PM25_EAST = PM25_EAST.replace(char, '')

for char in string.punctuation:
    PM25_CENTRAL = PM25_CENTRAL.replace(char, '')
for char in string.ascii_lowercase:
    PM25_CENTRAL = PM25_CENTRAL.replace(char, '')
    
for char in string.punctuation:
    PM25_SOUTH = PM25_SOUTH.replace(char, '')
for char in string.ascii_lowercase:
    PM25_SOUTH = PM25_SOUTH.replace(char, '')
    
for char in string.punctuation:
    PM25_NORTH = PM25_NORTH.replace(char, '')
for char in string.ascii_lowercase:
    PM25_NORTH = PM25_NORTH.replace(char, '')
    
PM25_WEST = ['Western Region PM2.5: ',int(PM25_WEST)]
PM25_EAST = ['Eastern Region PM2.5: ',int(PM25_EAST)]
PM25_CENTRAL = ['Central Region PM2.5: ',int(PM25_CENTRAL)]
PM25_SOUTH = ['Southern Region PM2.5: ',int(PM25_SOUTH)]
PM25_NORTH = ['Northern Region PM2.5: ',int(PM25_NORTH)]


PSI_WEST = goodsoup2[60]
PSI_EAST = goodsoup2[62]
PSI_CENTRAL = goodsoup2[63]
PSI_SOUTH = goodsoup2[64]
PSI_NORTH = goodsoup2[65]

for char in string.punctuation:
    PSI_WEST = PSI_WEST.replace(char, '')
for char in string.ascii_lowercase:
    PSI_WEST = PSI_WEST.replace(char, '')

for char in string.punctuation:
    PSI_EAST = PSI_EAST.replace(char, '')
for char in string.ascii_lowercase:
    PSI_EAST = PSI_EAST.replace(char, '')

for char in string.punctuation:
    PSI_CENTRAL = PSI_CENTRAL.replace(char, '')
for char in string.ascii_lowercase:
    PSI_CENTRAL = PSI_CENTRAL.replace(char, '')
    
for char in string.punctuation:
    PSI_SOUTH = PSI_SOUTH.replace(char, '')
for char in string.ascii_lowercase:
    PSI_SOUTH = PSI_SOUTH.replace(char, '')
    
for char in string.punctuation:
    PSI_NORTH = PSI_NORTH.replace(char, '')
for char in string.ascii_lowercase:
    PSI_NORTH = PSI_NORTH.replace(char, '')
    
PSI_WEST = ['Western Region PSI: ',int(PSI_WEST)]
PSI_EAST = ['Eastern Region PSI: ',int(PSI_EAST)]
PSI_CENTRAL = ['Central Region PSI: ',int(PSI_CENTRAL)]
PSI_SOUTH = ['Southern Region PSI: ',int(PSI_SOUTH)]
PSI_NORTH = ['Northern Region PSI: ',int(PSI_NORTH)]

if PSI_WEST[1] > 100:
    PSI_WEST.append(" | Air Quality Descriptor: Unhealthy")
if PSI_EAST[1] > 100:
    PSI_EAST.append(" | Air Quality Descriptor: Unhealthy")
if PSI_CENTRAL[1] > 100:
    PSI_CENTRAL.append(" | Air Quality Descriptor: Unhealthy")
if PSI_SOUTH[1] > 100:
    PSI_SOUTH.append(" | Air Quality Descriptor: Unhealthy")
if PSI_NORTH[1] > 100:
    PSI_NORTH.append(" | Air Quality Descriptor: Unhealthy")


if PSI_WEST[1] > 200:
    PSI_WEST.append(" | Air Quality Descriptor: *Very Unhealthy*")
if PSI_EAST[1] > 200:
    PSI_EAST.append(" | Air Quality Descriptor: *Very Unhealthy*")
if PSI_CENTRAL[1] > 200:
    PSI_CENTRAL.append(" | Air Quality Descriptor: *Very Unhealthy*")
if PSI_SOUTH[1] > 200:
    PSI_SOUTH.append(" | Air Quality Descriptor: *Very Unhealthy*")
if PSI_NORTH[1] > 200:
    PSI_NORTH.append(" | Air Quality Descriptor: *Very Unhealthy*")
    

if PSI_WEST[1] > 300:
    PSI_WEST.append(" | Air Quality Descriptor: *Hazardous*")
if PSI_EAST[1] > 300:
    PSI_EAST.append(" | Air Quality Descriptor: *Hazardous*")
if PSI_CENTRAL[1] > 300:
    PSI_CENTRAL.append(" | Air Quality Descriptor: *Hazardous*")
if PSI_SOUTH[1] > 300:
    PSI_SOUTH.append(" | Air Quality Descriptor: *Hazardous*")
if PSI_NORTH[1] > 300:
    PSI_NORTH.append(" | Air Quality Descriptor: *Hazardous*")

if PM25_WEST[1] > 55:
    PM25_WEST.append(" | Band: II")
if PM25_EAST[1] > 55:
    PM25_EAST.append(" | Band: II")
if PM25_CENTRAL[1] > 55:
    PM25_CENTRAL.append(" | Band: II")
if PM25_SOUTH[1] > 55:
    PM25_SOUTH.append(" | Band: II")
if PM25_NORTH[1] > 55:
    PM25_NORTH.append(" | Band: II")


if PM25_WEST[1] > 150:
    PM25_WEST.append(" | Band: *III*")
if PM25_EAST[1] > 150:
    PM25_EAST.append(" | Band: *III*")
if PM25_CENTRAL[1] > 150:
    PM25_CENTRAL.append(" | Band: *III*")
if PM25_SOUTH[1] > 150:
    PM25_SOUTH.append(" | Band: *III*")
if PM25_NORTH[1] > 150:
    PM25_NORTH.append(" | Band: *III*")
    

if PM25_WEST[1] > 250:
    PM25_WEST.append(" | Band: *IV*")
if PM25_EAST[1] > 250:
    PM25_EAST.append(" | Band: *IV*")
if PM25_CENTRAL[1] > 250:
    PM25_CENTRAL.append(" | Band: *IV*")
if PM25_SOUTH[1] > 250:
    PM25_SOUTH.append(" | Band: *IV*")
if PM25_NORTH[1] > 250:
    PM25_NORTH.append(" | Band: *IV*")

listofhaze = []
if len(PSI_WEST) > 2:
    listofhaze.append(PSI_WEST)
if len(PSI_EAST) > 2:
    listofhaze.append(PSI_EAST)
if len(PSI_CENTRAL) > 2:
    listofhaze.append(PSI_CENTRAL)
if len(PSI_SOUTH) > 2:
    listofhaze.append(PSI_SOUTH)
if len(PSI_NORTH) > 2:
    listofhaze.append(PSI_NORTH)
if len(PM25_WEST) > 2:
    listofhaze.append(PM25_WEST)
if len(PM25_EAST) > 2:
    listofhaze.append(PM25_EAST)
if len(PM25_CENTRAL) > 2:
    listofhaze.append(PM25_CENTRAL)
if len(PM25_SOUTH) > 2:
    listofhaze.append(PM25_SOUTH)
if len(PM25_NORTH) > 2:
    listofhaze.append(PM25_NORTH)
    
hazezones = []
PSIvalues = []
qualitydescriptors = []

for zone in listofhaze:
    hazezones.append(zone[0])
    PSIvalues.append(zone[1])
    qualitydescriptors.append(zone[2])

hazezone_msg = ""

for i in range (len(hazezones)):
    hazezone_msg = hazezone_msg + (hazezones[i] + str(PSIvalues[i]) + qualitydescriptors[i] + '\n')


print(psi)
print(hazezone_msg)


receiverlist = ["Team LMZ", "ERU, MOC, Zone, BM", "ne PWY", "Russ" ]

for receiver in receiverlist:
    try:
        (image_x, image_y) = pyautogui.locateCenterOnScreen(r"C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS PATCH 1\SEARCHICON.png", grayscale=True, confidence=.5)       # returns (left, top, width, height) of first place it is found
        
    except ImageNotFoundException:
        (image_x, image_y) = pyautogui.locateCenterOnScreen(r"C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS PATCH 1\SEARCHICON.png", grayscale=True, confidence=.5)

    #Click on Search Icon and Type Name and Enter Chat
    pyautogui.click(x=image_x, y=image_y, clicks=10, button='left')
    time.sleep(30)
    pyautogui.click(x=image_x, y=image_y, clicks=10, button='left')
    pyautogui.typewrite(receiver, interval=0.1)
    pyautogui.click(x=image_x, y=image_y, clicks=10, button='left')
    pyautogui.typewrite('\n', interval=0.1)
    print("Recipient " + receiver + " found.")
    time.sleep(10)
    

    #Check time before sending message "TEAM LMZ"
    if receiver == receiverlist[0] and (datetime.datetime.now().strftime('%H%M')) > '0730' and (datetime.datetime.now().strftime('%H%M')) < '2330' and (listofhaze != []):
        recipient = "Greetings " + receiverlist[0]    #"TEAM LMZ"
        send_msg(recipient, hazezone_msg)
        
    elif receiver == receiverlist[0] and (datetime.datetime.now().strftime('%H%M')) > '0030' and (datetime.datetime.now().strftime('%H%M')) < '0630'  and (listofhaze != []):
        recipient = "Good Evening " + receiverlist[0]
        send_msg(recipient, hazezone_msg)

    #Check time before sending message "ERU, MOC, Zone, BM"
    if receiver == receiverlist[1] and (datetime.datetime.now().strftime('%H%M')) > '0730' and (datetime.datetime.now().strftime('%H%M')) < '2330'  and (listofhaze != []):
        recipient = "Hello " + "ERU"
        send_msg(recipient, hazezone_msg)
        
    elif receiver == receiverlist[1] and (datetime.datetime.now().strftime('%H%M')) > '0000' and (datetime.datetime.now().strftime('%H%M')) < '0630'  and (listofhaze != []):
        recipient = "Attention " + "all Maintenance Teams"
        send_msg(recipient, hazezone_msg)
        
    #Check time before sending message "One PWY"
    if receiver == receiverlist[2] and (datetime.datetime.now().strftime('%H%M')) > '0730' and (datetime.datetime.now().strftime('%H%M')) < '2330' and (listofhaze != []):
        recipient = "Greetings " + "PWY"   #"TEAM LMZ"
        send_msg(recipient, hazezone_msg)
        
    elif receiver == receiverlist[2] and (datetime.datetime.now().strftime('%H%M')) > '0030' and (datetime.datetime.now().strftime('%H%M')) < '0630'  and (listofhaze != []):
        recipient = "Good Evening " + "PWY"
        send_msg(recipient, hazezone_msg)

    #Check time before sending message
    if receiver == receiverlist[3] and (datetime.datetime.now().strftime('%H%M')) > '0730' and (datetime.datetime.now().strftime('%H%M')) < '2330'  and (listofhaze != []):
        recipient = "Hello "+ receiverlist[3] #"Hello ERU"
        send_msg(recipient, hazezone_msg)

        time.sleep(10800)#last person triggers delay
        
    elif receiver == receiverlist[3] and (datetime.datetime.now().strftime('%H%M')) > '0030' and (datetime.datetime.now().strftime('%H%M')) < '0630'  and (listofhaze != []):
        recipient = "Hi " + receiverlist[3] #"Attention all Maintenance Teams"
        send_msg(recipient, hazezone_msg)

        time.sleep(10800)#last person triggers delay
    
