import cv2 as cv


# reading images
img = cv.imread('photos/dog1.jpeg',0)

# display the image as new window
cv.imshow('dog1',img)

# wait for delay in miliseconds
# here in this case it will wait for infinte amount of time for key press from keyboard
cv.waitKey(0)