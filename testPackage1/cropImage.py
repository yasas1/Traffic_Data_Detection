import numpy as np
import cv2

image = cv2.imread('image3.png')
y=400
x=600
h=500
w=700
crop = image[y:y+h, x:x+w]
cv2.imshow('Image', crop)
#cv2.imwrite('CropDirBinary.png',crop)
