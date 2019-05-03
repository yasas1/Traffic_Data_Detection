from PIL import Image
col = Image.open("test4.png") #read image
gray = col.convert('L')  #conversion to gray scale
bw = gray.point(lambda x: 0 if x<200 else 255, '1')  #binarization
#bw.save("trainedBinary.png") #save it
bw.save("testBinary4.png")
