import random
import string
import numpy as np


def random_ascii():
    return random.choice(string.printable[:-6])

def generate_ascii_array(row, col):
    return np.array([[random_ascii() for _ in range(col)] for _ in range(row)])


if __name__ == '__main__':
    arr = generate_ascii_array(27, 48)
    # print(arr.shape)
    for row in arr:
        print(''.join(row))
