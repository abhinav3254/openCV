import cv2

img = cv2.imread("../res/kraiti.png")


# printing the size of the image
print(img.shape)
# output :- (225, 225, 3)
# first 255 is the height
# second 255 is the width
# 3 is the number for channels which is BGR


# now we are resizing the image
# here 101 is the width and 100 is the height
# here in this case first width will be there and then we have height
imgResize = cv2.resize(img,(101,100))
print(imgResize.shape)


# image itself is an array of matrix or pixels
# for crop we can delete elements of array
# note here height comes first and then width comes second
imgCropped = img[0:100,100:250]
# this 0:100 means we started from index 0 and goes upto 100
# same for 100:250 we started from 100 and goes upto 250


cv2.imshow("original_img",img)
cv2.imshow("resized_img",imgResize)
cv2.imshow("cropped_img",imgCropped)




cv2.waitKey(0)