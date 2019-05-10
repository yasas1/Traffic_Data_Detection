import cv2   
import numpy as np

import webbrowser

webbrowser.open('https://www.google.com/maps/dir/Lumbini+Bus+Stop,+Sri+Sambuddhathva+Jayanthi+Mawatha,+Colombo/University+of+Colombo,+College+House,+Kumaratunga+Munidasa+Mawatha,+Colombo/@6.8909493,79.8561933,15z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x3ae25bce93e5496f:0x622bcc171fe22cd4!2m2!1d79.8677945!2d6.8844459!1m5!1m1!1s0x3ae2596309dfdd3f:0x45a4b0e7834ac0d4!2m2!1d79.8587938!2d6.9000149')


import pyautogui
import time

#x=1

#while x<4:
 #   pyautogui.screenshot('\Users\Dell\Desktop\screenshot\image'+str(x)+'.png')
  #  x+=1
   # time.sleep(2)
#time.sleep(6)

time.sleep(3)

scr = pyautogui.screenshot()
scr.save('image3.png')
