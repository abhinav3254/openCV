import numpy as np
import cv2 as cv


# Accessing and Modifying pixel values
img = cv.imread('photos/dog1.jpeg',1)
pixel = img[100,100]


print(pixel)