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



cv2.waitKey(0)