from PIL import Image
col = Image.open("CropDir.png") #read image
gray = col.convert('L')  #conversion to gray scale
bw = gray.point(lambda x: 0 if x<185 else 255, '1')  #binarization
#bw.save("trainedBinary5.png") #save it

bw.save("dirBinary.png")