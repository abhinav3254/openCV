import numpy as np
import cv2

# Capturing video through webcam
webcam = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    _, imageFrame = webcam.read()

    # Convert the frame to HSV color space
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)

    # Set range for red color and define mask
    red_lower = np.array([0, 100, 100], np.uint8)  # Adjusted lower bound for red
    red_upper = np.array([10, 255, 255], np.uint8)  # Adjusted upper bound for red
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    # Set range for green color and define mask
    green_lower = np.array([40, 40, 40], np.uint8)  # Adjusted lower bound for green
    green_upper = np.array([80, 255, 255], np.uint8)  # Adjusted upper bound for green
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    # Set range for blue color and define mask
    blue_lower = np.array([100, 100, 100], np.uint8)  # Adjusted lower bound for blue
    blue_upper = np.array([140, 255, 255], np.uint8)  # Adjusted upper bound for blue
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)

    # Create a kernel for morphological operations
    kernel = np.ones((5, 5), "uint8")

    # For red color
    red_mask = cv2.dilate(red_mask, kernel)
    res_red = cv2.bitwise_and(imageFrame, imageFrame, mask=red_mask)

    # For green color
    green_mask = cv2.dilate(green_mask, kernel)
    res_green = cv2.bitwise_and(imageFrame, imageFrame, mask=green_mask)

    # For blue color
    blue_mask = cv2.dilate(blue_mask, kernel)
    res_blue = cv2.bitwise_and(imageFrame, imageFrame, mask=blue_mask)

    # Find contours for red color
    contours, hierarchy = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            # Draw a rectangle around the detected red object
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # Display "Red Colour" text near the rectangle
            cv2.putText(imageFrame, "Red Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255))

    # Find contours for green color
    contours, hierarchy = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            # Draw a rectangle around the detected green object
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            # Display "Green Colour" text near the rectangle
            cv2.putText(imageFrame, "Green Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))

    # Find contours for blue color
    contours, hierarchy = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 300:
            x, y, w, h = cv2.boundingRect(contour)
            # Draw a rectangle around the detected blue object
            imageFrame = cv2.rectangle(imageFrame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # Display "Blue Colour" text near the rectangle
            cv2.putText(imageFrame, "Blue Colour", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))

    # Display the resulting frame with color detection
    cv2.imshow("Multiple Color Detection in Real-Time", imageFrame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release the video capture and close all OpenCV windows
webcam.release()
cv2.destroyAllWindows()
