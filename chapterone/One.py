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

'''

# this is for webcam

# here we have one web cam in our system so we are using 0
# if we have multiple then we going to mention our ID here
cap = cv2.VideoCapture(0)
# 3 is id number for width and width is 640
cap.set(3,640)
# 4 is id number of height and height is 480
cap.set(4,480)
# here 10 is the id for brightness and 100 is the value
cap.set(10,100)

while True:
    success,img = cap.read()
    cv2.imshow("video_window",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
