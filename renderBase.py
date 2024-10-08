"""
The abstract class of ascii char render

input: ascii char array -- np.ndarray
output: image of given resolution -- np.ndarray
"""

import cv2
from abc import ABC, abstractmethod
import numpy as np


class RenderBase(ABC):
    def __init__(self, output_resolution: tuple, font, scale, thickness, color):
        """
        Constructor takes in a tuple of (width, height),
        defining the output image shape as class attributes
        """
        self.height = output_resolution[0]
        self.width = output_resolution[1]

        # TODO: parameters could be customized
        self.font = font
        self.font_scale = scale
        self.font_thickness = thickness
        self.font_color = color

    @abstractmethod
    def ascii_frame(self, ascii_array) -> np.ndarray:
        """
        Return the image of ascii characters

        input: 2D ascii char array
        output: image of ascii frame
        """
        pass
