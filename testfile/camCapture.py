"""
TESTING CLASS, CAPTURING VIDEO
"""

import cv2
import time
import numpy as np

# Open the default camera
cam = cv2.VideoCapture(0)

# Get the default frame width and height
# Capture-Property-Frame-Width
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
                   )  # Capture-Property-Frame-Height

# Define the codec(coder/decoder) and create VideoWriter object
# Four Character Code for codec is `mp4v`
codec = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.mp4', codec, 20, (frame_width, frame_height))

prev_time = time.time()

while True:
    ret, frame = cam.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # green_channel = frame.copy()
    # green_channel[:, :, 0] = 0
    # green_channel[:, :, 2] = 0
    # blue_channel = frame.copy()
    # blue_channel[:, :, 1] = 0
    # blue_channel[:, :, 2] = 0
    # red_channel = frame.copy()
    # red_channel[:, :, 0] = 0
    # red_channel[:, :, 1] = 0
    # gray_frame = 0.114 * blue_channel + 0.587 * green_channel + 0.299 * red_channel

    # frame = gray_frame / 225

    if not ret:
        break

    curr_time = time.time()
    fps = 1 / (curr_time - prev_time)
    prev_time = curr_time

    text = f"FPS: {int(fps)}"
    cv2.putText(frame, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                1, (255, 255, 255), 2, cv2.LINE_AA)

    # Write the frame to the output file
    # out.write(frame)

    # Display the captured frame
    cv2.imshow('Camera', frame)

    prev_time = time.time()

    # Press 'q' to exit the loop
    if cv2.waitKey(1) == ord('q'):
        break

# Release the capture and writer objects
cam.release()
# out.release()
cv2.destroyAllWindows()
