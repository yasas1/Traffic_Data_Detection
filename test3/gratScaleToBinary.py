from PIL import Image
col = Image.open("test7crop.png") #read image
gray = col.convert('L')  #conversion to gray scale
bw = gray.point(lambda x: 0 if x<205 else 255, '1')  #binarization
#bw.save("trainedBinary5.png") #save it
bw.save("testBinary8.png")
