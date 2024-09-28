"""
The abstract class of image to ascii converter
mapping grayscale value to ascii char

input: low resolution image -- ndarray
output: ascii scheme array
"""

from abc import ABC, abstractmethod
import numpy as np

class CvtBase(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def ascii_scheme(self, reduced_image) -> np.ndarray:
        """
        Return the array scheme of ascii characters

        input: reduced resolution image -- np.ndarray
        output: 2D ascii char array
        """
        pass
