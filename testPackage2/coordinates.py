from PIL import Image
from pylab import *

# read image to array
im = array(Image.open('newIm1.png'))

y=0
x=500
h=1000
w=1400
crop = im[y:y+h, x:x+w]

# plot the image
imshow(crop)

# some points
x = [100,100,400,400]
y = [200,500,200,500]

# plot the points with red star-markers
plot(x,y,'r*')

# line plot connecting the first two points
plot(x[:2],y[:2])

# add title and show the plot
title('Plotting: "empire.jpg"')
show()
