import numpy as np
import cv2

image = cv2.imread('dirBinary.png')
y=50#400
x=218#600
h=600#500
w=366#700
crop = image[y:y+h, x:x+w]
cv2.imshow('Image', crop)
#cv2.imwrite('CropDirBinary.png',crop)
