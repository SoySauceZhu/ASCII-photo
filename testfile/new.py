import numpy as np
import cv2
import random
import string

# Generate random ASCII character
def random_ascii():
    return random.choice(string.printable[:-6])  # Printable ASCII without whitespace/control characters

# Create a 144x256 ndarray of ASCII characters
ascii_array = np.array([[random_ascii() for _ in range(256)] for _ in range(144)])

# Create a blank canvas with resolution 1080x1920
canvas_width = 1920
canvas_height = 1080
canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

# Set font, scale, and thickness
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.4  # Scaling to fit characters within the grid cells
font_thickness = 1
font_color = (255, 255, 255)  # White color for characters

# Calculate cell size (pixel size for each ASCII character)
rows, cols = ascii_array.shape
cell_width = canvas_width // cols  # width of each cell
cell_height = canvas_height // rows  # height of each cell

# Render the ASCII array onto the canvas
for i in range(rows):
    for j in range(cols):
        char = ascii_array[i, j]
        x = j * cell_width
        y = i * cell_height + int(cell_height * 0.8)  # Adjust y to vertically center text
        cv2.putText(canvas, char, (x, y), font, font_scale, font_color, font_thickness)

# Display the result
cv2.imshow('ASCII Art', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
