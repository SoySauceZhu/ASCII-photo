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


class ProcessBase(ABC):
    def __init__(self, reduced_resolution: tuple):
        """
        Constructor takes in a tuple of (width, height),
        defining the output image shape as class attributes
        """
        self.height = reduced_resolution[0]
        self.width = reduced_resolution[1]

    @abstractmethod
    def downscale_image(self, input_image) -> np.ndarray:
        """
        Return the image (array) of reduced image 

        input: origin frame image from webcam (grayscale -- i.e. [1080, 1920])
        output: reduced image (array) 
        """
        pass
