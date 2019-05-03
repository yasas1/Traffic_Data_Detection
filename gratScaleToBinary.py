from PIL import Image
col = Image.open("image2.png") #read image
gray = col.convert('L')  #conversion to gray scale
bw = gray.point(lambda x: 0 if x<180 else 255, '1')  #binarization
bw.save("trainedBinary.png") #save it
bw.save("trafficBinary.png")
