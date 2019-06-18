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
driver.get("https://www.google.com/maps/dir/6.8463651,79.9481864/6.896591,79.8599699/@6.8662918,79.8862328,14z/data=!4m2!4m1!3e0")

time.sleep(4)

x=1

while x<4:
    
    scr = pyautogui.screenshot()
    scr.save(r"D:\Traffic Data\Traffic_Data_Detection\Image\newIm"+str(x)+".png")
    x+=1
    time.sleep(refreshrate)
    driver.refresh()

driver.close()
