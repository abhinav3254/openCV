import cv2

print('package imported')

# read the image
img = cv2.imread("res/brock.png")

# show the image
cv2.imshow("window_name",img)

# add a delay show that images will not close automatically
cv2.waitKey(0)