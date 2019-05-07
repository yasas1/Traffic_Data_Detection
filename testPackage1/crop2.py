import numpy as np
import cv2

image = cv2.imread('22.png')
y=220
x=1000
h=650
w=400
crop = image[y:y+h, x:x+w]
cv2.imshow('Image', crop)
cv2.imwrite('22crop.png',crop)
