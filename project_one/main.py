import cv2
import mediapipe as mp
import pyautogui


webcam = cv2.VideoCapture(0)
myHands = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils


while True:
    # this read() function returns two things
    # first _ we don't need it
    _,image = webcam.read()
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output = myHands.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image,hand)

    cv2.imshow("live_cam", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


webcam.release()
cv2.destroyAllWindows()