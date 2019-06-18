import cv2   
import numpy as np
import pyautogui
import time

import webbrowser
from selenium import webdriver

import urllib
#import urllib2


refreshrate=5

driver = webdriver.Chrome(r"C:\Users\Dell\Desktop\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com/maps/dir/6.8463651,79.9481864/6.896591,79.8599699/@6.8662918,79.8862328,14z/data=!4m54!4m53!1m50!3m4!1m2!1d79.9393007!2d6.845248!3s0x3ae250682f00494d:0xb3223fc5ca65ec1d!3m4!1m2!1d79.9280032!2d6.8462467!3s0x3ae25070682e7fd5:0x792f4ecc1c1e2889!3m4!1m2!1d79.9180013!2d6.8523242!3s0x3ae25a818b422539:0x923c01b80ee9e89c!3m4!1m2!1d79.9085055!2d6.8576863!3s0x3ae25a7d5994531d:0x2a37c5767636c8e2!3m4!1m2!1d79.8957831!2d6.8653539!3s0x3ae25a5d11b9748d:0xe8556d56c2bd22c8!3m4!1m2!1d79.8898743!2d6.8692086!3s0x3ae25a4493c0a9a7:0xc7d2cbc87034819b!3m4!1m2!1d79.8818254!2d6.8739059!3s0x3ae25a493df7e8f1:0x849ea1c09d4842e5!3m4!1m2!1d79.8772802!2d6.8779967!3s0x3ae25a358182749f:0x4dd98114c8846ede!3m4!1m2!1d79.8701652!2d6.8811899!3s0x3ae25bcbb794fba3:0xe1c76798a63e6088!3m4!1m2!1d79.8632871!2d6.8911247!3s0x3ae25bd08119f627:0x3d1a22e4b7cb4754!1m0!3e0")


time.sleep(6)
driver.refresh()
x=1

while x<4:
    
    time.sleep(3)
    scr = pyautogui.screenshot()
    
    scr.save(r"D:\Traffic Data\Traffic_Data_Detection\Image\newIm"+str(x)+".png")
    
    x+=1
    time.sleep(refreshrate)
    driver.refresh()

driver.close()
