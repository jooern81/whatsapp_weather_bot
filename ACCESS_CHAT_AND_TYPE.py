# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 15:38:50 2019

@author: chinjooern
"""

import pyautogui
import time
from pyscreeze import ImageNotFoundException

try:
     (image_x, image_y) = pyautogui.locateCenterOnScreen('TOHWEIQI.png')       # returns (left, top, width, height) of first place it is found
     print("WHATSAPP GROUP FOUND")
except ImageNotFoundException:
    (image_x, image_y) = pyautogui.locateCenterOnScreen('TOHWEIQI_CLICKED.png')
    print("WHATSAPP GROUP FOUND")
        
        
pyautogui.click(x=image_x, y=image_y, clicks=1, button='left')
time.sleep(0.1)
pyautogui.typewrite('The Weather is Bad\n', interval=0.05)

#pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)

#pyautogui.locateOnScreen('looksLikeThis.png')       # returns (left, top, width, height) of first place it is found

#pyautogui.typewrite('Hello world!\n', interval=secs_between_keys)