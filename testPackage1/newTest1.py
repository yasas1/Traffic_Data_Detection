import numpy as np
import cv2

image = cv2.imread('33.png')

y=220
x=1000
h=645
w=400

routeDetected = image[y:y+h, x:x+w]

#cv2.imwrite('routeDetected.png',routeDetected)

cv2.imshow('Original',image)

#image[368,159]=[0,0,0]
cv2.circle(image,(447,63), 63, (0,0,255), -1)

cv2.imshow('routeDetected',routeDetected)
    

