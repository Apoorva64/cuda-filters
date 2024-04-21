import numpy as np
from numba import cuda


def create_array(size):
    arr = np.zeros(size, dtype=np.float32)
    # Transfer the array to the device
    d_arr = cuda.to_device(arr)
    return arr, d_arr


@cuda.jit
def local_id_in_arr(arr):
    i = cuda.grid(1)
    if i < arr.size:
        arr[i] = cuda.threadIdx.x


@cuda.jit
def global_id_in_arr(arr):
    i = cuda.grid(1)
    if i < arr.size:
        arr[i] = i
