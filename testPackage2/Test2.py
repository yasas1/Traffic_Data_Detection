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
driver.get("https://www.google.com/maps/@6.8874059,79.8676187,14.78z/data=!5m1!1e1")
time.sleep(4)

x=1

while x<4:
    
    scr = pyautogui.screenshot()
    scr.save(r"D:\Traffic Data\Traffic_Data_Detection\Image\newIm"+str(x)+".png")
    x+=1
    time.sleep(refreshrate)
    driver.refresh()

driver.close()
