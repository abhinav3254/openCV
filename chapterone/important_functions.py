import cv2

import numpy as np

# define our kernel
# uint8 means that the values can range in between 0 to 255
kernel = np.ones((5,5),np.uint8)

img = cv2.imread("res/krati.png")

# first we will convert this image into grayscale
# this cvtColor() will convert our image into various color spaces
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# making image blur
# (7,7) is our knumber -> kernal number it can be odd numbers like 3x3 or 7x7 etc
# sigmaX is 0
imgBlur = cv2.GaussianBlur(img,(7,7),0)

# canny
imgCanny = cv2.Canny(img,150,200)

# image dilate
# for thickness border like we use dilation
imgDilate = cv2.dilate(imgCanny,kernel,iterations=1)

# opposite of dilate
imgEroded = cv2.erode(imgDilate,kernel,iterations=1)

cv2.imshow("original_image",img)
cv2.imshow("window_name",imgGray)
cv2.imshow("blur_img",imgBlur)
cv2.imshow("canny_img",imgCanny)
cv2.imshow("image_dialation",imgDilate)
cv2.imshow("image_erode",imgEroded)


cv2.waitKey(0)