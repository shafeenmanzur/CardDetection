import cv2
import numpy as np
import sys

# Input IP Address for IP Webcam or 0 for physical webcam
try:
    # If using command line arguments
    ip_address = sys.argv[1]
except:
    # Physically write in the variable here. 0 for Hardware Webcam. Or IP address for IP webcam
    ip_address = ''

cap = cv2.VideoCapture(ip_address)
tmp = 43
tester = 0
while cap.isOpened():
    # Variables housing threshold for Contour Capture
    q, w = 50, 200
    # reads frames from a camera
    ret, frame = cap.read()

    # Display an original image
    cv2.imshow('Original', frame)

    # Find edges in the input image and marks them in the output map edges
    edges = cv2.Canny(frame, q, w)
    # Display edges in a frame
    cv2.imshow('Edges', edges)

    # Determines the coordinates and area of all Edges present in current frame.
    # Sorts them from smallest to largest area
    contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    sorted_contours = sorted(contours, key=cv2.contourArea, reverse=False)
    testRect = sorted_contours[-1]
    x, y, w, h = cv2.boundingRect(testRect)
    currArea = w * h
    # Display the Contoured Image with the highest area. Checks to see if area changes and updates image accordingly.
    if currArea > 25000:
        if tmp != currArea:
            tmp = currArea
            try:
                # Can input function here utilizing the captured card image
                pass
            except:
                pass
        crop_img = frame[y:y + h, x:x + w]
        cv2.imshow("cropped", crop_img)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    # Debugging tool to control Contour Threshold (Press Q/E to change upper threshold | A/D to change lower threshold)
    elif k == 101:
        q += 10
        print(q)
    elif k == 113:
        q -= 10
        print(q)
    elif k == 97:
        w -= 10
        print(w)
    elif k == 100:
        w += 10
        print(w)

cap.release()
cv2.destroyAllWindows()
