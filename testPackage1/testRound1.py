import numpy as np
import cv2

image = cv2.imread('33.png')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

retval, QueryImgBGR = cv2.threshold(gray, 185, 255, cv2.THRESH_BINARY)

#-----------Route detecting

MIN_MATCH_COUNT = 30

detector = cv2.xfeatures2d.SIFT_create()
FLANN_INDEX_KDTREE = 0
index_params =dict(algorithm = FLANN_INDEX_KDTREE, trees = 5 )

flann = cv2.FlannBasedMatcher(index_params, {})

trainImg=cv2.imread("dirBinaryTrained.png",0)
trainKP,trainDesc=detector.detectAndCompute(trainImg,None)

#QueryImgBGR=cv2.imread("dirBinary.png")
QueryImg=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
queryKP,queryDesc=detector.detectAndCompute(QueryImg,None)
matches=flann.knnMatch(queryDesc,trainDesc,k=2)

goodMatch=[]
for m,n in matches:
    if(m.distance<0.75*n.distance):
        goodMatch.append(m)

MIN_MATCH_COUNT=30
if(len(goodMatch)>=MIN_MATCH_COUNT):
    tp=[]
    qp=[]

    for m in goodMatch:
        tp.append(trainKP[m.trainIdx].pt)
        qp.append(queryKP[m.queryIdx].pt)

    tp,qp=np.float32((tp,qp))

    H,status=cv2.findHomography(tp,qp,cv2.RANSAC,3.0)

    h,w=trainImg.shape
    
    trainBorder=np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])

    queryBorder=cv2.perspectiveTransform(trainBorder,H)

    y = min(np.int32(queryBorder[0][3][1]),np.int32(queryBorder[0][0][1]))
    x = min(np.int32(queryBorder[0][0][0]),np.int32(queryBorder[0][1][0]))
    
    routeDetected = image[y:y+h, x:x+w]
    
    print("y+h",y+h)
    print("x+w",x+w)
    
    cv2.imshow('Original',image)
    
#---------------color detecting
    
    hsv=cv2.cvtColor(routeDetected,cv2.COLOR_BGR2HSV)

    #----------- Orange color

    orange_lower=np.array([10,155,255],np.uint8)
    orange_upper=np.array([80,255,255],np.uint8)
        #mask for orange
    orange=cv2.inRange(hsv, orange_lower, orange_upper)

    kernal = np.ones((5 ,5), "uint8")

    orange=cv2.dilate(orange, kernal)
    
    #Tracking the Orange Color
    (_,contours,hierarchy)=cv2.findContours(orange,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        #print(area)
        if(area>150):
            x,y,w,h = cv2.boundingRect(contour)
            print("orange x",x)
            print("orange y",y)
            colorteDetected = cv2.rectangle(routeDetected,(x,y),(x+w,y+h),(0, 160, 255),2)
            cv2.putText(colorteDetected,"Orange",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0, 128, 255))
            
    #-------------- Red Color

    red_lower=np.array([160,100,100],np.uint8)
    red_upper=np.array([180,255,255],np.uint8)

    red=cv2.inRange(hsv, red_lower, red_upper)

    kernal = np.ones((5 ,5), "uint8")

    red=cv2.dilate(red, kernal)

    #Tracking the Red Color
    (_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        #print(area)
        if(area>150):
            x,y,w,h = cv2.boundingRect(contour)
            print("red x",x)
            print("red y",y)
            colorteDetected = cv2.rectangle(colorteDetected,(x,y),(x+w,y+h),(0, 0, 255),2)
            cv2.putText(colorteDetected,"Red",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0, 0, 255))

    cv2.imshow("Color Detecting",colorteDetected)
    cv2.imwrite('Detected2.png',colorteDetected)
    

else:
    print("Not Enough match found- %d/%d"%(len(goodMatch),MIN_MATCH_COUNT))




    

