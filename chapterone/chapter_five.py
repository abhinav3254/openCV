import cv2
import numpy as np

img = cv2.imread("res/cards.png")


# this file we are trying to get one card out from the image of many cards

width = 250
height = 350
points1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
points2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(points1,points2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("img_window",img)
cv2.imshow(("output"),imgOutput)


cv2.waitKey(0)