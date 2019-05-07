import numpy as np
import cv2

img = cv2.imread('test7crop.png')


#img = np.zeros((400, 400, 3), dtype = "uint8") 
  
# Creating rectangle 
cv2.rectangle(img, (200, 150), (300, 450), (0, 255, 0), 3) 
  
cv2.imshow('dark', img) 
