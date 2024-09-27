"""
The abstract class of image to ascii converter
mapping grayscale value to ascii char

input: low resolution image -- ndarray
output: ascii scheme array
"""

from abc import ABC, abstractmethod
import numpy as np

class CvtBase(ABC):
    def __init__(self, output_resolution : tuple):
        """
        Constructor takes in a tuple of (width, height),
        defining the output ascii array shape as class attributes
        """
        self.height = output_resolution[0]
        self.width = output_resolution[1]

    @abstractmethod
    def ascii_scheme(reduced_image) -> np.ndarray:
        """
        Return the array scheme of ascii characters

        input: reduced resolution image -- np.ndarray
        output: 2D ascii char array
        """
        pass
