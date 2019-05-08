import numpy as np
import cv2

MIN_MATCH_COUNT = 30

detector = cv2.xfeatures2d.SIFT_create() #cv2.SIFT()
FLANN_INDEX_KDTREE = 0
index_params =dict(algorithm = FLANN_INDEX_KDTREE, trees = 5 )

flann = cv2.FlannBasedMatcher(index_params, {})

trainImg=cv2.imread("dirBinaryTrained.png",0)
trainKP,trainDesc=detector.detectAndCompute(trainImg,None)

#cam=cv2.VideoCapture(0)

#while True:
    #ret, QueryImgBGR=cam.read()
QueryImgBGR=cv2.imread("dirBinary.png")
QueryImg=cv2.cvtColor(QueryImgBGR,cv2.COLOR_BGR2GRAY)
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
    print(h)
    print(w)
    
    trainBorder=np.float32([[[0,0],[0,h-1],[w-1,h-1],[w-1,0]]])
    print(trainBorder)
    queryBorder=cv2.perspectiveTransform(trainBorder,H)
    print(np.int32(queryBorder))
    print(np.int32(queryBorder[0][0][0]))

    cv2.polylines(QueryImgBGR,[np.int32(queryBorder)],True,(0,255,0),5)
else:
    print("Not Enough match found- %d/%d"%(len(goodMatch),MIN_MATCH_COUNT))

cv2.imshow('result',QueryImgBGR)

#cv2.destroyAllWindows()

