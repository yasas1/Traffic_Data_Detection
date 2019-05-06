import numpy as np
import cv2

img = cv2.imread('tt.png')


#img = np.zeros((400, 400, 3), dtype = "uint8") 
  
# Creating rectangle 
cv2.rectangle(img, (250, 50), (250, 450), (0, 255, 0), 3) 
  
cv2.imshow('dark', img) 
