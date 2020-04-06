import cv2
import numpy as np

img = cv2.imread("newIm1.png")

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

color = hsv[58,67]

print(color)

cv2.rectangle(img,(58,67),(65,72),(0, 0, 0),2)
cv2.rectangle(img,(70,70),(75,75),(0,0,0),2)

cv2.imshow('pixel Color',img)
