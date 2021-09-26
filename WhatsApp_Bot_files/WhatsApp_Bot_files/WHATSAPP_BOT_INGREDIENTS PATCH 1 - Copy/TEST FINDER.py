# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:46:09 2019

@author: joo
"""
import pyautogui
import sys
import cv2

print(sys.path)

(image_x, image_y) = pyautogui.locateCenterOnScreen('start.png')  

print(image_x)