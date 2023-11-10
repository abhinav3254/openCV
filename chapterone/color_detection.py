import cv2
import numpy as np

def empty():
    pass

img = cv2.imread("res/brock.png")

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)


imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)


cv2.imshow("org_img",img)
cv2.imshow("hsv_img",imgHSV)

cv2.waitKey(0)