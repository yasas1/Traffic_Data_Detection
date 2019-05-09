import numpy as np
import cv2

image = cv2.imread('CropDir.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

retval, threshold = cv2.threshold(gray, 185, 255, cv2.THRESH_BINARY)

cv2.imshow('threshold',threshold)

