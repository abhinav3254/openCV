import numpy as np
import cv2 as cv

# # Accessing and Modifying pixel values
# img = cv.imread('photos/dog1.jpeg',1)
# pixel = img[100,100]
# print(pixel)

# Accessing Image Properties

img = cv.imread('photos/dog1.jpeg',1)

# generating image properties
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
size1 = img.size

print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)
print('Image Size  :', size1)


