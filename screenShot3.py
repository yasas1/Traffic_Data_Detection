
import numpy as np
import pyautogui
import time

import webbrowser
from selenium import webdriver

import urllib
#import urllib2

refreshrate=input("Enter the number of seconds")
refreshrate=int(refreshrate)
driver = webdriver.Chrome(r"C:\Users\Dell\Desktop\chromedriver.exe")
driver.get("https://www.google.com/maps/@6.8874059,79.8676187,14.78z/data=!5m1!1e1")
while True:
    time.sleep(refreshrate)
    driver.refresh()


