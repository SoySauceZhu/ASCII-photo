"""
The abstract base class of image procrssor
Takes in original frame image, convert to grayscale,
maps to ascii array and returen the ascii scheme

Image processor should
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

        reduced_resolution: int, the height of output ascii scheme (reduced image)
        chars: string, chars from high density to low
        aspect_ratio: tuple, i.e. (16, 9)
        """
        self.reduced_rows = reduced_resolution
        self.reduced_cols = reduced_resolution * aspect_ratio[0] // aspect_ratio[1]
        self.chars = chars[::-1]
        self.aspect_ratio = aspect_ratio

    @abstractmethod
    def ascii_array(self, input_image) -> np.ndarray:
        """
        Takes in the original frame image
        Return the ascii scheme (np.array) of reduced image 

        input: origin frame image from webcam (i.e. [1080, 1920, 3])
        output: ascii scheme (array) 
        """
        pass
