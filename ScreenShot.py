import cv2   
import numpy as np

import webbrowser

webbrowser.open('https://www.google.com/maps/@6.8899724,79.8636689,14.96z/data=!5m1!1e1')

import pyautogui
import time

#x=1

#while x<4:
 #   pyautogui.screenshot('\Users\Dell\Desktop\screenshot\image'+str(x)+'.png')
  #  x+=1
   # time.sleep(2)
#time.sleep(6)

#scr = pyautogui.screenshot()
#scr.save('image23.png')

img = cv2.imgread("image23.png")


hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#definig the range of red color
red_lower=np.array([136,87,111],np.uint8)
red_upper=np.array([180,255,255],np.uint8)

#finding the range of red,blue and yellow color in the image
red=cv2.inRange(hsv, red_lower, red_upper)


#Morphological transformation, Dilation  	
kernal = np.ones((5 ,5), "uint8")

red=cv2.dilate(red, kernal)
res=cv2.bitwise_and(img, img, mask = red)

#Tracking the Red Color
(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
for pic, contour in enumerate(contours):
    area = cv2.contourArea(contour)
    
    if(area>300):
        x,y,w,h = cv2.boundingRect(contour)	
	img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2) cv2.putText(img,"RED color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255))
	
#cv2.imshow("Redcolour",red)
cv2.imshow("Color Tracking",img)
#cv2.imshow("red",res) 	
if cv2.waitKey(10) & 0xFF == ord('q'):
    cap.release()
    cv2.destroyAllWindows()
    break







































    
