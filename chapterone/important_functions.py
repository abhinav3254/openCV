import cv2


img = cv2.imread("res/krati.png")

# first we will convert this image into grayscale
# this cvtColor() will convert our image into various color spaces
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("window_name",imgGray)

cv2.waitKey(0)