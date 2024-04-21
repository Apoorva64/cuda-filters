from unittest import TestCase

from numba import cuda

from lab1 import first_kernel


class Test(TestCase):
    def test_print_hello(self):
        first_kernel.print_hello[1, 4]()
        cuda.synchronize()
        # hello is printed 4 times

    def test_print_hello_grid(self):
        first_kernel.print_hello[2, 4]()
        cuda.synchronize()
        # hello is printed 8 times