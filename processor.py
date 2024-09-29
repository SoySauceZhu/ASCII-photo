"""
Reference: https://scipython.com/blog/ascii-art/
"""
import cv2
import numpy as np
from processBase import ProcessBase


class Processor(ProcessBase):
    def __init__(self, reduced_resolution: int, chars="$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`\\'.   ", aspect_ratio=(4, 3)):
        super().__init__(reduced_resolution, chars, aspect_ratio)

    def map_value(self, x):
        return int(x) * (len(self.chars) - 1) // 255

    def ascii_array(self, input_image):
        reduced = self.preprocess(input_image)
        output = np.array([[self.chars[self.map_value(reduced[row, col])] for col in range(
            reduced.shape[1])] for row in range(reduced.shape[0])])
        return output

    def preprocess(self, image):
        aspect_ratio = self.aspect_ratio
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
        height, width = image.shape

        if width / height > aspect_ratio[0] / aspect_ratio[1]:  # Wider than 4:3
            new_width = int(height * aspect_ratio[0] / aspect_ratio[1])
            new_height = height
        else:
            new_width = width
            new_height = int(width * aspect_ratio[1] / aspect_ratio[0])

        x_start = (width - new_width) // 2
        y_start = (height - new_height) // 2

        cropped_image = image[y_start:y_start +
                              new_height, x_start:x_start + new_width]

        resized_image = cv2.resize(
            cropped_image, (self.reduced_cols, self.reduced_rows))
        enhanced_image = cv2.equalizeHist(resized_image)

        return enhanced_image


if __name__ == '__main__':
    m = Processor(96)
    image = cv2.imread("resource/mingjie.jpg")
    output = m.ascii_array(image)
    import sys
    np.set_printoptions(threshold=sys.maxsize)

    print(output)
