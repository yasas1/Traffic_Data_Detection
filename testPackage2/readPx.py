import cv2


img = cv2.imread("rdPix.png",1)

px=img[606,527]

print(px)

print(img.shape)


