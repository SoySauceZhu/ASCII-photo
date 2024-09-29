"""
The abstract base class of
mosaic (dimensional reduction) processor

Dimensional reduction image processor should
inherit from this interface
and implement api in the class

input: image (np.ndarray)
output: ascii array (np.ndarray)
"""

from abc import ABC, abstractmethod
import numpy as np


class ProcessBase(ABC):
    def __init__(self, reduced_resolution: int, chars, aspect_ratio):
        """
        Constructor takes in a tuple of (width, height),
        defining the output image shape as class attributes
        """
        self.reduced_rows = reduced_resolution
        self.reduced_cols = reduced_resolution * aspect_ratio[0] // aspect_ratio[1]
        self.chars = chars[::-1]
        self.aspect_ratio = aspect_ratio

    @abstractmethod
    def ascii_array(self, input_image) -> np.ndarray:
        """
        Return the image (array) of reduced image 

        input: origin frame image from webcam (grayscale -- i.e. [1080, 1920])
        output: reduced image (array) 
        """
        pass
