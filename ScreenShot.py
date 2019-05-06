import cv2   
import numpy as np

import webbrowser

webbrowser.open('https://www.google.com/maps/@6.888194,79.8661988,14.74z/data=!5m1!1e1')

import pyautogui
import time

#x=1

#while x<4:
 #   pyautogui.screenshot('\Users\Dell\Desktop\screenshot\image'+str(x)+'.png')
  #  x+=1
   # time.sleep(2)
#time.sleep(6)

time.sleep(2)

scr = pyautogui.screenshot()
scr.save('image2.png')
