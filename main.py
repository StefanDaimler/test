import os
import math
import numpy as np


def func1(a, b):
    return math.floor(a + b)


def func2(a, b, c):
    return sum(a, b, c)


print(func1(1, 2), func2(3, 4, 5))
np.array((1,2,3))