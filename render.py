import cv2
import numpy as np
from renderBase import RenderBase


class Render(RenderBase):
    def __init__(self, output_resolution: tuple, font=cv2.FONT_HERSHEY_PLAIN, scale=1, thickness=1, color=(255,255,255)):
        super().__init__(output_resolution, font, scale, thickness, color)

    def ascii_frame(self, ascii_array):
        canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        rows, cols = ascii_array.shape
        x_spacing = self.width // cols
        y_spacing = self.height // rows

        for row in range(rows):
            for col in range(cols):
                position = (col * x_spacing, row *
                            y_spacing + int(y_spacing * 0.8))
                cv2.putText(canvas, ascii_array[row, col], position, self.font, self.font_scale,
                            self.font_color, self.font_thickness, cv2.LINE_AA)

        return canvas


if __name__ == '__main__':
    import testfile.randomAscii as rand
    import time

    render = Render((1080, 1920))

    prev_time = time.time()

    while True:
        array = rand.generate_ascii_array(96, 128)
        image = render.ascii_frame(array)

        curr_time = time.time()
        fps = 1 / (curr_time - prev_time)
        prev_time = curr_time

        text = f"FPS: {int(fps)}"
        cv2.putText(image, text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2, cv2.LINE_AA)

        cv2.imshow("image", image)

        prev_time = time.time()

        if cv2.waitKey(1) == ord('q'):
            break