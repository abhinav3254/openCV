import cv2
import numpy as np


'''
# now we creating our matrix
# since this is grayscale image so we add three channels to make it a color image
# img = np.zeros((512,512))
# print(img.shape)

img = np.zeros((512,512,3))
print(img)
# now we are going to add color to the images
# this [:] means for all
# img[:] = 255,0,0
# 200 is height and 300 is width
img[200:300,100:300] = 255,0,0
# here this will only add color to that one which values we have entered

cv2.imshow("image_window",img)

'''

# now we going to create lines
img = np.zeros((256,256,3))


# here we are creating a line
# (0,0) is the starting point from where we are going to start
# (200,200) is the ending point upto which we are going to end
# and (0,255,0) is the color code for the line
cv2.line(img,(0,0),(200,200),(0,255,0),3)

cv2.imshow("img_window",img)

cv2.waitKey(0)