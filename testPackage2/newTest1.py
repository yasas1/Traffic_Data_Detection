import numpy as np
import cv2

image = cv2.imread('33.png')

y=220
x=1000
h=645
w=400

routeDetected = image[y:y+h, x:x+w]

cv2.imwrite('routeDetected.png',routeDetected)

route = cv2.imread('routeDetected.png')

#route_hsv = cv2.cvtColor(routeDetected,cv2.COLOR_BGR2HSV)

#route[40,50]=[0, 160, 255]
#cv2.circle(image,(447,63), 63, (0,0,255), -1)

colorDetected = cv2.rectangle(route,(58,67),(65,72),(0, 160, 255),2)

cv2.imshow('routeDetected',colorDetected)
    

