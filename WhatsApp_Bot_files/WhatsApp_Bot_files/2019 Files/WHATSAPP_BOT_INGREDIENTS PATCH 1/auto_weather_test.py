# -*- coding: utf-8 -*-
"""
Created on Thu May  2 11:25:32 2019

@author: chinjooern
"""
import random
import requests
import string
import emoji
import datetime
import pyautogui
import time
# import cv2

from pyscreeze import ImageNotFoundException
from bs4 import BeautifulSoup

#emojis
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

#page = requests.get("https://api.data.gov.sg/v1/environment/2-hour-weather-forecast")
#print(page.content)
html_doc = """
{"area_metadata":[{"name":"Ang Mo Kio","label_location":{"latitude":1.375,"longitude":103.839}},{"name":"Bedok","label_location":{"latitude":1.321,"longitude":103.924}},{"name":"Bishan","label_location":{"latitude":1.350772,"longitude":103.839}},{"name":"Boon Lay","label_location":{"latitude":1.304,"longitude":103.701}},{"name":"Bukit Batok","label_location":{"latitude":1.353,"longitude":103.754}},{"name":"Bukit Merah","label_location":{"latitude":1.277,"longitude":103.819}},{"name":"Bukit Panjang","label_location":{"latitude":1.362,"longitude":103.77195}},{"name":"Bukit Timah","label_location":{"latitude":1.325,"longitude":103.791}},{"name":"Central Water Catchment","label_location":{"latitude":1.38,"longitude":103.805}},{"name":"Changi","label_location":{"latitude":1.357,"longitude":103.987}},{"name":"Choa Chu Kang","label_location":{"latitude":1.377,"longitude":103.745}},{"name":"Clementi","label_location":{"latitude":1.315,"longitude":103.76}},{"name":"City","label_location":{"latitude":1.292,"longitude":103.844}},{"name":"Geylang","label_location":{"latitude":1.318,"longitude":103.884}},{"name":"Hougang","label_location":{"latitude":1.361218,"longitude":103.886}},{"name":"Jalan Bahar","label_location":{"latitude":1.347,"longitude":103.67}},{"name":"Jurong East","label_location":{"latitude":1.326,"longitude":103.737}},{"name":"Jurong Island","label_location":{"latitude":1.266,"longitude":103.699}},{"name":"Jurong West","label_location":{"latitude":1.34039,"longitude":103.705}},{"name":"Kallang","label_location":{"latitude":1.312,"longitude":103.862}},{"name":"Lim Chu Kang","label_location":{"latitude":1.423,"longitude":103.717332}},{"name":"Mandai","label_location":{"latitude":1.419,"longitude":103.812}},{"name":"Marine Parade","label_location":{"latitude":1.297,"longitude":103.891}},{"name":"Novena","label_location":{"latitude":1.327,"longitude":103.826}},{"name":"Pasir Ris","label_location":{"latitude":1.37,"longitude":103.948}},{"name":"Paya Lebar","label_location":{"latitude":1.358,"longitude":103.914}},{"name":"Pioneer","label_location":{"latitude":1.315,"longitude":103.675}},{"name":"Pulau Tekong","label_location":{"latitude":1.403,"longitude":104.053}},{"name":"Pulau Ubin","label_location":{"latitude":1.404,"longitude":103.96}},{"name":"Punggol","label_location":{"latitude":1.401,"longitude":103.904}},{"name":"Queenstown","label_location":{"latitude":1.291,"longitude":103.78576}},{"name":"Seletar","label_location":{"latitude":1.404,"longitude":103.869}},{"name":"Sembawang","label_location":{"latitude":1.445,"longitude":103.818495}},{"name":"Sengkang","label_location":{"latitude":1.384,"longitude":103.891443}},{"name":"Sentosa","label_location":{"latitude":1.243,"longitude":103.832}},{"name":"Serangoon","label_location":{"latitude":1.357,"longitude":103.865}},{"name":"Southern Islands","label_location":{"latitude":1.208,"longitude":103.842}},{"name":"Sungei Kadut","label_location":{"latitude":1.413,"longitude":103.756}},{"name":"Tampines","label_location":{"latitude":1.345,"longitude":103.944}},{"name":"Tanglin","label_location":{"latitude":1.308,"longitude":103.813}},{"name":"Tengah","label_location":{"latitude":1.374,"longitude":103.715}},{"name":"Toa Payoh","label_location":{"latitude":1.334304,"longitude":103.856327}},{"name":"Tuas","label_location":{"latitude":1.294947,"longitude":103.635}},{"name":"Western Islands","label_location":{"latitude":1.205926,"longitude":103.746}},{"name":"Western Water Catchment","label_location":{"latitude":1.405,"longitude":103.689}},{"name":"Woodlands","label_location":{"latitude":1.432,"longitude":103.786528}},{"name":"Yishun","label_location":{"latitude":1.418,"longitude":103.839}}],"items":[{"update_timestamp":"2019-05-31T10:03:53+08:00","timestamp":"2019-05-31T10:00:00+08:00","valid_period":{"start":"2019-05-31T10:00:00+08:00","end":"2019-05-31T12:00:00+08:00"},
"forecasts":[{"area":"Ang Mo Kio","forecast":"Shower (Day)"},{"area":"Bedok","forecast":"Rain (Day)"},{"area":"Bishan","forecast":"Rain (Day)"},{"area":"Boon Lay","forecast":"Partly Cloudy (Day)"},{"area":"Bukit Batok","forecast":"Shower (Day)"},{"area":"Bukit Merah","forecast":"Partly Cloudy (Day)"},{"area":"Bukit Panjang","forecast":"Partly Cloudy (Day)"},{"area":"Bukit Timah","forecast":"Rain (Day)"},{"area":"Central Water Catchment","forecast":"Partly Cloudy (Day)"},{"area":"Changi","forecast":"Partly Cloudy (Day)"},{"area":"Choa Chu Kang","forecast":"Partly Cloudy (Day)"},{"area":"Clementi","forecast":"Partly Cloudy (Day)"},{"area":"City","forecast":"Partly Cloudy (Day)"},{"area":"Geylang","forecast":"Partly Cloudy (Day)"},{"area":"Hougang","forecast":"Partly Cloudy (Day)"},{"area":"Jalan Bahar","forecast":"Partly Cloudy (Day)"},{"area":"Jurong East","forecast":"Partly Cloudy (Day)"},{"area":"Jurong Island","forecast":"Partly Cloudy (Day)"},{"area":"Jurong West","forecast":"Partly Cloudy (Day)"},{"area":"Kallang","forecast":"Partly Cloudy (Day)"},{"area":"Lim Chu Kang","forecast":"Partly Cloudy (Day)"},{"area":"Mandai","forecast":"Partly Cloudy (Day)"},{"area":"Marine Parade","forecast":"Rain (Day)"},{"area":"Novena","forecast":"Partly Cloudy (Day)"},{"area":"Pasir Ris","forecast":"Partly Cloudy (Day)"},{"area":"Paya Lebar","forecast":"Partly Cloudy (Day)"},{"area":"Pioneer","forecast":"Partly Cloudy (Day)"},{"area":"Pulau Tekong","forecast":"Partly Cloudy (Day)"},{"area":"Pulau Ubin","forecast":"Partly Cloudy (Day)"},{"area":"Punggol","forecast":"Partly Cloudy (Day)"},{"area":"Queenstown","forecast":"Partly Cloudy (Day)"},{"area":"Seletar","forecast":"Partly Cloudy (Day)"},{"area":"Sembawang","forecast":"Partly Cloudy (Day)"},{"area":"Sengkang","forecast":"Partly Cloudy (Day)"},{"area":"Sentosa","forecast":"Partly Cloudy (Day)"},{"area":"Serangoon","forecast":"Partly Cloudy (Day)"},{"area":"Southern Islands","forecast":"Partly Cloudy (Day)"},{"area":"Sungei Kadut","forecast":"Partly Cloudy (Day)"},{"area":"Tampines","forecast":"Partly Cloudy (Day)"},{"area":"Tanglin","forecast":"Partly Cloudy (Day)"},{"area":"Tengah","forecast":"Partly Cloudy (Day)"},{"area":"Toa Payoh","forecast":"Partly Cloudy (Day)"},{"area":"Tuas","forecast":"Partly Cloudy (Day)"},{"area":"Western Islands","forecast":"Partly Cloudy (Day)"},{"area":"Western Water Catchment","forecast":"Partly Cloudy (Day)"},{"area":"Woodlands","forecast":"Partly Cloudy (Day)"},{"area":"Yishun","forecast":"Partly Cloudy (Day)"}]}],"api_info":{"status":"healthy"}}
"""
soup = BeautifulSoup(html_doc, "html.parser")
goodsoup = soup.prettify()

# Clean up soup
for char in string.punctuation:
    goodsoup = goodsoup.replace(char, '')

bestsoup = goodsoup.split('Ang Mo Kio')
forecast = "Ang Mo Kio" + bestsoup[2]
listforecast = forecast.split("area")
listforecast[len(listforecast) - 1] = listforecast[len(listforecast) - 1].split("api").pop(0)

for i in range(len(listforecast)):
    listforecast[i] = listforecast[i].split("forecast")

# Set up Area divisions
listofrain = []  # create the list of rainy areas
listofrainzones = []

# Assign Addresses to Areas
NZareas = {'Ang Mo Kio': 'Ang Mo Kio\nYio Chu Kang\n', 'Bishan': 'Bishan\nMarymount\n', 'Sembawang': 'Sembawang\nCanberra\n',
           'Sungei Kadut':'Kranji', 'Toa Payoh':'Braddell\nToa Payoh\nCaldecott\n',
            'Woodlands': 'Marsiling\nWoodlands\nAdmiralty\n', 'Yishun': 'Khatib\n'}
CENTRALareas = {'Bukit Merah': 'Outram Park\nTiong Bahru\nRedhill\nLabrador Park\nTelok Blangah\nHarbourfront\n',
                'Bukit Timah': 'Holland Village\n',
                'City': 'Dhoby Ghaut\nCity Hall\nRaffles Place\nBugis\nTanjong Pagar\nBras Basah\nEsplanade\nPromenade\nNicoll Highway\nMarina Bay\n Marina South Pier\n',
                'Kallang': 'Kallang\nLavendar\nStadium\nMountbatten\n', 'Novena': 'Novena\nNewton\nOrchard\nSomerset\n',
                'Queenstown': 'Queenstown\nCommonwealth\nBuona Vista\nDover\nOne North\nKent Ridge\nHaw Par Villa\nPasir Panjang\n’,‘Tanglin’: ‘Botanic Gardens\nFarrer Road\n'}
EZareas = {'Bedok': 'Tanah Merah\nBedok\nKembangan\n', 'Changi': 'Changi\n',
            'Geylang': 'Eunos\nPaya Lebar\nAljunied\nDakota\nMacpherson\n', 'Hougang': 'Pasir Ris\n',
            'Tampines': 'Tampiness\nSemei\nExpo', 'Serangoon': 'Bartley\nSerangoon\nLorong Chuan\n'}
#SZareas = ['Marine Parade', 'City', 'Bukit Merah', 'Clementi', 'Queenstown']
WZareas = {'Bukit Batok': 'Bukit Batok\nBukit Gombak\n', 'Choa Chu Kang': 'Choa Chu Kang\nYew Tee\n',
            'Clementi': 'Clementi\n', 'Jurong East': 'Lakeside\nBoonLay\nPioneer\n', 'Pioneer':'Joo Koon\nGul Circle\n',
            'Tuas': 'Tuas Cresent\nTuas West Road\nTuas Link\n'}

MRT_Stations = ['']
# Determine Rain Areas
for i in range(len(listforecast)):
    if "Shower" in listforecast[i][1] or "Rain" in listforecast[i][1]:
        listofrain.append(listforecast[i])

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
                rainzone_msg = rainzone_msg + '\nNorthen Zone: \n'
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
                rainzone_msg = rainzone_msg + '\nCentral Zone: \n'
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
                rainzone_msg = rainzone_msg + '\nEastern Zone: \n'
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
                rainzone_msg = rainzone_msg + '\nWestern Zone: \n'
                header = 1
            rainzone_msg = rainzone_msg + WZareas[key]
header = 1

recipient = "Team LMZ"
WeatherIntroMessages = [
        recipient + ','+ Ewarn+ ' do take note that the following stations may experience rain in the next 2 hours'+Ewarn+': \n',
        recipient + ', expect rain in the following'+ Etrain + 'stations in the next 2 hours: \n',
        recipient + ', there is chance of'+ Edrops + 'rain' +Edrops+' affecting the stations stated below: \n',
        recipient + ', you may have to get your'+ Epayung + 'out if you are in the following stations for the next 2 hours:\n',
        recipient + ', Dark' + Ecloud + 'detected, expect rain in the next 2 hours for the stations listed below\n']
WeatherOutroMessages = [' \nPlease drive and work safely, your safety is our priority.',
            ' \nRainy weather makes the roads more dangerous, think of your family, drive and work safely. ',
            ' \nWork and drive carefully, all it takes is one accident.' + Ehospital,
            ' \nPlease work and drive carefully, life is valuable. ' + Ecar,
            ' \nYour life is precious, drive slowly and work carefully.' + Econtractor,
            ' \nTake the necessary safety precautions and work safely.' + Econtractor,
            ' \nCasual + Safety = Casualty, your attitude counts, so take safety seriously' +Eokay,
            ' \nSlip and Falls can lead to serious injury, otherwise it can be pretty emberassing' + Esmirk,
            ' \nLife did not begin by accident. Dont end it as one.' + Erelieve]

WhatsApp_Message = (WeatherIntroMessages[random.randint(0, len(WeatherIntroMessages) - 1)] + rainzone_msg +
                        WeatherOutroMessages[random.randint(0, len(WeatherOutroMessages) - 1)])
print(WhatsApp_Message)

#print(Esmirk)

## Find WhatsApp Group 1
#try:
#    (image_x, image_y) = pyautogui.locateCenterOnScreen(r"C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS\TOHWEIQI.png",
#                                                        grayscale=True,
#                                                        confidence=.5)  # returns (left, top, width, height) of first place it is found
#    print("WHATSAPP GROUP 1 FOUND")
#except ImageNotFoundException:
#    (image_x, image_y) = pyautogui.locateCenterOnScreen(
#        r"C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS\TOHWEIQI_CLICKED.png", grayscale=True, confidence=.5)
#    print("WHATSAPP GROUP 1 FOUND")
#
## Click on WhatsApp Group 1
#pyautogui.click(x=image_x, y=image_y, clicks=1, button='left')
#
## Check time before sending message
#if (datetime.datetime.now().strftime('%H%M')) > '0730' and (datetime.datetime.now().strftime('%H%M')) < '2230' and (
#listofrainzones) != []:
#    recipient = "Team LMZ"
#    WeatherIntroMessages = [
#        recipient + ', do take note that the following regions may experience rain in the next 2 hours: ',
#        recipient + ', expect rain in the following regions in the next 2 hours: ']
#    WeatherOutroMessages = [' Please drive and work safely, your safety is our priority.',
#                            ' Rainy weather makes the roads more dangerous, think of your family, drive and work safely. ',
#                            ' Work and drive carefully, all it takes is one accident.',
#                            ' Please work and drive carefully, life is valuable. ',
#                            ' Your life is precious, drive slowly and work carefully.']
#    WhatsApp_Message = (WeatherIntroMessages[random.randint(0, len(WeatherIntroMessages) - 1)] + str(listofrainzones) +
#                        WeatherOutroMessages[random.randint(0, len(WeatherOutroMessages) - 1)])
#    print(WhatsApp_Message)
#    time.sleep(10)
#    pyautogui.typewrite(WhatsApp_Message + '\n', interval=0.001)
#
#if (datetime.datetime.now().strftime('%H%M')) < '0730' and (listofrainzones) != []:
#    recipient = "Good evening LMZ"
#    WeatherIntroMessages = [
#        recipient + ', do take note that the following regions may experience rain in the next 2 hours: ',
#        recipient + ', expect rain in the following regions in the next 2 hours: ']
#    WeatherOutroMessages = [
#        ' Please drive safely, and seek shelter at the nearest station if necessary, your safety is our priority.',
#        ' Rainy weather makes work more dangerous, think of your family, work safely. ',
#        ' Proceed to the nearest station for shelter if necessary and drive carefully, all it takes is one accident.',
#        ' Proceed to the nearest station for shelter if necessary ahd drive slowly and carefully, life is valuable. ',
#        ' Your life is precious, seek shelter if necessary and drive carefully.']
#    WhatsApp_Message = (WeatherIntroMessages[random.randint(0, len(WeatherIntroMessages) - 1)] + str(listofrainzones) +
#                        WeatherOutroMessages[random.randint(0, len(WeatherOutroMessages) - 1)])
#    print(WhatsApp_Message)
#    time.sleep(10)
#    pyautogui.typewrite(WhatsApp_Message + '\n', interval=0.001)
#
## Find WhatsApp Group 2
#try:
#    (image_x, image_y) = pyautogui.locateCenterOnScreen(r"C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS\ERUMOC.png",
#                                                        grayscale=True,
#                                                        confidence=.5)  # returns (left, top, width, height) of first place it is found
#    print("WHATSAPP GROUP 2 FOUND")
#except ImageNotFoundException:
#    (image_x, image_y) = pyautogui.locateCenterOnScreen(
#        r"C:\Users\joo\Desktop\WHATSAPP_BOT_INGREDIENTS\ERUMOC_CLICKED.png", grayscale=True, confidence=.5)
#    print("WHATSAPP GROUP 2 FOUND")
#
## Click on WhatsApp Group 2
#pyautogui.click(x=image_x, y=image_y, clicks=1, button='left')
#
## Check time before sending message
#if (datetime.datetime.now().strftime('%H%M')) > '0730' and (datetime.datetime.now().strftime('%H%M')) < '2230' and (
#listofrainzones) != []:
#    recipient = "Hello ERU"
#    WeatherIntroMessages = [
#        recipient + ', do take note that the following regions may experience rain in the next 2 hours: ',
#        recipient + ', expect rain in the following regions in the next 2 hours: ']
#    WeatherOutroMessages = [' Please drive and work safely, your safety is our priority.',
#                            ' Rainy weather makes the roads more dangerous, think of your family, drive and work safely. ',
#                            ' Work and drive carefully, all it takes is one accident.',
#                            ' Please work and drive carefully, life is valuable. ',
#                            ' Your life is precious, drive slowly and work carefully.']
#    WhatsApp_Message = (WeatherIntroMessages[random.randint(0, len(WeatherIntroMessages) - 1)] + str(listofrainzones) +
#                        WeatherOutroMessages[random.randint(0, len(WeatherOutroMessages) - 1)])
#    print(WhatsApp_Message)
#    time.sleep(10)
#    pyautogui.typewrite(WhatsApp_Message + '\n', interval=0.001)
#
#if (datetime.datetime.now().strftime('%H%M')) < '0730' and (listofrainzones) != []:
#    recipient = "Attention all Maintenance Teams"
#    WeatherIntroMessages = [
#        recipient + ', do take note that the following regions may experience rain in the next 2 hours: ',
#        recipient + ', expect rain in the following regions in the next 2 hours: ']
#    WeatherOutroMessages = [
#        ' Please drive safely, and seek shelter at the nearest station if necessary, your safety is our priority.',
#        ' Rainy weather makes work more dangerous, think of your family, work safely. ',
#        ' Proceed to the nearest station for shelter if necessary and drive carefully, all it takes is one accident.',
#        ' Proceed to the nearest station for shelter if necessary ahd drive slowly and carefully, life is valuable. ',
#        ' Your life is precious, seek shelter if necessary and drive carefully.']
#    WhatsApp_Message = (WeatherIntroMessages[random.randint(0, len(WeatherIntroMessages) - 1)] + str(listofrainzones) +
#                        WeatherOutroMessages[random.randint(0, len(WeatherOutroMessages) - 1)])
#    print(WhatsApp_Message)
#    time.sleep(10)
#    pyautogui.typewrite(WhatsApp_Message + '\n', interval=0.001)
#
#:sunny:
#:umbrella:
#:cloud:
#:zap:
#:partly_sunny:
#:sweat_drops: