import numpy as np
import cv2

image = cv2.imread('newIm1.png')
y=0
x=500
h=1000
w=1400
crop = image[y:y+h, x:x+w]
cv2.imshow('Image', crop)
#cv2.imwrite('tt.png',crop)
