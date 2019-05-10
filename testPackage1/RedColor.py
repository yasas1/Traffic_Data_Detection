import cv2   
import numpy as np

img = cv2.imread("CropDirTest.png")

hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

red_lower=np.array([160,100,100],np.uint8)
red_upper=np.array([180,255,255],np.uint8)

red=cv2.inRange(hsv, red_lower, red_upper)

kernal = np.ones((5 ,5), "uint8")

red=cv2.dilate(red, kernal)
#res=cv2.bitwise_and(img, img, mask = red)

#Tracking the Red Color
(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    print(area)
    if(area>150):
        x,y,w,h = cv2.boundingRect(contour)
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0, 0, 255),2)
        cv2.putText(img,"Red",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0, 0, 255))


orange_lower=np.array([10,155,255],np.uint8)
orange_upper=np.array([80,255,255],np.uint8)

orange=cv2.inRange(hsv, orange_lower, orange_upper)

kernal = np.ones((5 ,5), "uint8")

orange=cv2.dilate(orange, kernal)
#res=cv2.bitwise_and(img, img, mask = red)

#Tracking the Red Color
(_,contours,hierarchy)=cv2.findContours(orange,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    print(area)
    if(area>150):
        x,y,w,h = cv2.boundingRect(contour)
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(0, 128, 255),2)
        cv2.putText(img,"Orange",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0, 128, 255))


cv2.imshow("Color Tracking",img)

if(cv2.waitKey(10) & 0xFF == ord('q')):
    cap.release()
    cv2.destroyAllWindows()
    
