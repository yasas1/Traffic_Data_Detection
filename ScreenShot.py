import cv2   
import numpy as np

import webbrowser

#webbrowser.open('https://www.google.com/maps/dir/Lumbini+Bus+Stop,+Sri+Sambuddhathva+Jayanthi+Mawatha,+Colombo/University+of+Colombo,+College+House,+Kumaratunga+Munidasa+Mawatha,+Colombo/@6.8909493,79.8561933,15z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x3ae25bce93e5496f:0x622bcc171fe22cd4!2m2!1d79.8677945!2d6.8844459!1m5!1m1!1s0x3ae2596309dfdd3f:0x45a4b0e7834ac0d4!2m2!1d79.8587938!2d6.9000149')

webbrowser.open('https://www.google.com/maps/dir/Kottawa+Town,+Pannipitiya/6.8477483,79.9257858/Delkanda,+Avissawella+Road,+Nugegoda/Nugegoda+Flyover,+High+Level+Road,+Nugegoda/6.8825857,79.8692621/6.8968387,79.8599586/@6.8696969,79.8978907,13z/data=!4m23!4m22!1m5!1m1!1s0x3ae2504b3e254457:0xd5f578935488b98f!2m2!1d79.9654324!2d6.8411652!1m0!1m5!1m1!1s0x3ae25a66db9d519f:0xbb077ad082d16898!2m2!1d79.9002016!2d6.8632231!1m5!1m1!1s0x3ae25a4500eccc4f:0x55bf8720feb93177!2m2!1d79.8882487!2d6.8698731!1m0!1m0!3e0')


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
scr.save('new1.png')
