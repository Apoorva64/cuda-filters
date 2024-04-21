import numpy as np
from numba import cuda


@cuda.jit
def print_hello():
    print("Hello")

