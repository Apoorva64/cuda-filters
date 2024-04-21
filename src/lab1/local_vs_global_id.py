from numba import cuda


@cuda.jit
def coordinates1d():
    print("The thread local id is", cuda.threadIdx.x, "The block local id is", cuda.blockIdx.x, "The global id is",
          cuda.grid(1))


@cuda.jit
def coordinates2d():
    print("The thread local id is", cuda.threadIdx.x, cuda.threadIdx.y, "The block local id is", cuda.blockIdx.x,
          cuda.blockIdx.y, "The global id is", cuda.grid(2)[0], cuda.grid(2)[1])
