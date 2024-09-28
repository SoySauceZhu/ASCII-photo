import cv2
import numpy as np
from renderBase import RenderBase


class Render(RenderBase):
    def __init__(self, output_resolution: tuple):
        super().__init__(output_resolution)
        # TODO: parameters could be customized
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.font_scale = 0.4
        self.font_thickness = 1
        self.font_color = (255, 255, 255)

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
    render = Render((1080, 1920))


    while True:
        array = rand.generate_ascii_array(96, 128)
        image = render.ascii_frame(array)

        cv2.imshow("image", image)

        if cv2.waitKey(1) == ord('q'):
            break