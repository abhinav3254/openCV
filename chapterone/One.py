import cv2

'''
# this code for images
print('package imported')

# read the image
img = cv2.imread("res/brock.png")

# show the image
cv2.imshow("window_name",img)

# add a delay show that images will not close automatically
cv2.waitKey(0)
'''

# this code is for video

# this will import the video
cap = cv2.VideoCapture("res/video/brockvideo.mp4")

# now we need to display this video and video is sequence of images
# we need loop to go in each frame one by one

while True:
    success,img = cap.read()
    cv2.imshow("video_window",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break