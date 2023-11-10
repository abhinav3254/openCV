import cv2
import numpy as np

img = cv2.imread("res/brock.png")


'''
# adding both images side by side
imgHor = np.hstack((img,img))

imgVertical = np.vstack((img,img))

cv2.imshow("window_hor",imgHor)
cv2.imshow("window_vert",imgVertical)

# issue with this way of joining two images
# 1. Both images must have same channels if they don't have same number of channels then we can't join both of them
# 2. This way we can't resize the image

'''

# solution for the above problem

cv2.waitKey(0)