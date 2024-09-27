"""
The abstract base class of
mosaic (dimensional reduction) processor

Dimensional reduction image processor should
inherit from this interface
and implement api in the class

input: image (np.ndarray)
output: image (np.ndarray)
"""

from abc import ABC, abstractmethod
import numpy as np

class CvtBase(ABC):
    def __init__(self, output_resolution : tuple):
        """
        Constructor takes in a tuple of (width, height),
        defining the output image shape as class attributes
        """
        self.height = output_resolution[0]
        self.width = output_resolution[1]

    @abstractmethod
    def downscale_image(input_image) -> np.ndarray:
        """
        Return the image (array) of reduced image 

        input: origin frame image from webcam
        output: reduced image (array) 
        """
        pass