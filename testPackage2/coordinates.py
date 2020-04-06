from PIL import Image
from pylab import *

# read image to array
im = array(Image.open('img_0_1.png').convert(mode='RGB'))

y=0
x=500
h=1000
w=1400
#crop = im[y:y+h, x:x+w]

# plot the image
imshow(im)

# some points
x = [291,286,280,269,256,246,239,228,219,206,197,189,182,176,172,170,167,165,161,152,144,137,135,131,127,122,116,110,104,95,93,96,101]
y = [571,554,535,505,479,458,443,426,415,399,386,368,352,334,314,296,273,258,239,223,210,192,174,154,136,124,112,95,78,60,46,27,14]

# plot the points with red star-markers
plot(x,y,'b*')

# line plot connecting the first two points
#plot(x[:2],y[:2])

# add title and show the plot
title('Plotting: "empire.jpg"')
show()
