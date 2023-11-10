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


'''
# now we going to create lines
img = np.zeros((256,256,3))


# here we are creating a line
# (0,0) is the starting point from where we are going to start
# (200,200) is the ending point upto which we are going to end
# and (0,255,0) is the color code for the line
# cv2.line(img,(0,0),(200,200),(0,255,0),3)

# instead of specific lenght and height we are going to make it start it from start and end it to the end
# img.shape[1] --> height ,img.shape[0]--> width)
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

cv2.imshow("img_window",img)

'''

# creating an image
img = np.zeros((512,512,3))
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# here we are drawing the rectange and (0,0) is the starting index
# (255,350) --> is the ending index
# (0,0,255) is the color code
# 2 is the thickness
cv2.rectangle(img,(0,0),(255,350),(0,0,255),2)

# now filling the image
cv2.rectangle(img,(0,0),(255,350),(0,0,255),cv2.FILLED)

# now creating the circle
cv2.circle(img,(400,50),30,(255,0,0),5)


cv2.imshow("img_window",img)

cv2.waitKey(0)