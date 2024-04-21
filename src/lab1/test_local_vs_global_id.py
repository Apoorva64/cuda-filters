from unittest import TestCase


class Test(TestCase):
    def test_coordinates1d_w_1_block_8_threads(self):
        from lab1.local_vs_global_id import coordinates1d
        coordinates1d[1, 8]()
        """
        The thread local id is 0 The block local id is 0 The global id is 0
        The thread local id is 1 The block local id is 0 The global id is 1
        The thread local id is 2 The block local id is 0 The global id is 2
        The thread local id is 3 The block local id is 0 The global id is 3
        The thread local id is 4 The block local id is 0 The global id is 4
        The thread local id is 5 The block local id is 0 The global id is 5
        The thread local id is 6 The block local id is 0 The global id is 6
        The thread local id is 7 The block local id is 0 The global id is 7
        """

    def test_coordinates1d_w_2_blocks_8_threads(self):
        from lab1.local_vs_global_id import coordinates1d
        coordinates1d[2, 8]()
        """
        The thread local id is 0 The block local id is 1 The global id is 8
        The thread local id is 1 The block local id is 1 The global id is 9
        The thread local id is 2 The block local id is 1 The global id is 10
        The thread local id is 3 The block local id is 1 The global id is 11
        The thread local id is 4 The block local id is 1 The global id is 12
        The thread local id is 5 The block local id is 1 The global id is 13
        The thread local id is 6 The block local id is 1 The global id is 14
        The thread local id is 7 The block local id is 1 The global id is 15
        The thread local id is 0 The block local id is 0 The global id is 0
        The thread local id is 1 The block local id is 0 The global id is 1
        The thread local id is 2 The block local id is 0 The global id is 2
        The thread local id is 3 The block local id is 0 The global id is 3
        The thread local id is 4 The block local id is 0 The global id is 4
        The thread local id is 5 The block local id is 0 The global id is 5
        The thread local id is 6 The block local id is 0 The global id is 6
        The thread local id is 7 The block local id is 0 The global id is 7
        """
        # We can see that the thread local id is reset to 0 for each block

    def test_coordinates2d_w_1_block_4_2_1_threads(self):
        from lab1.local_vs_global_id import coordinates2d
        coordinates2d[1, (4, 2, 1)]()
        """
        The thread local id is 0 0 The block local id is 0 0 The global id is 0 0
        The thread local id is 1 0 The block local id is 0 0 The global id is 1 0
        The thread local id is 2 0 The block local id is 0 0 The global id is 2 0
        The thread local id is 3 0 The block local id is 0 0 The global id is 3 0
        The thread local id is 0 1 The block local id is 0 0 The global id is 0 1
        The thread local id is 1 1 The block local id is 0 0 The global id is 1 1
        The thread local id is 2 1 The block local id is 0 0 The global id is 2 1
        The thread local id is 3 1 The block local id is 0 0 The global id is 3 1
        """

    def test_coordinates2d_w_2_blocks_2_2_1_threads(self):
        from lab1.local_vs_global_id import coordinates2d
        coordinates2d[2, (2, 2, 1)]()
