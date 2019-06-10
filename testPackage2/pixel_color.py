import cv2
import numpy as np
img = cv2.imread("test_img.jpg")

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

color = hsv[58,67]

print(color)

cv2.rectangle(img,(58,67),(65,72),(0, 160, 255),2)
cv2.rectangle(img,(70,70),(75,75),(51,67,236),2)

cv2.imshow('pixel Color',img)
