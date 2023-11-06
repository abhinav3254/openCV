import cv2 as cv


# now see the diff here, when ever user pass flag as 1 it is considered as
# color image and if the flag is 0 then it is considered as greyscale
img = cv.imread('photos/dog2.jpeg',1)
cv.imshow('greyscale img',img)

cv.waitKey(0)
