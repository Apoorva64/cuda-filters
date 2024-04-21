from unittest import TestCase


class Test(TestCase):
    def test_local_id_in_arr_32_arr_1_block_32_threads(self):
        from lab1.memory_transfer import create_array, local_id_in_arr
        arr, d_arr = create_array(32)
        local_id_in_arr[1, 32](d_arr)
        arr = d_arr.copy_to_host()
        self.assertTrue(all(arr == range(32)))

    def test_local_id_in_arr_30_arr_1_blocks_32_threads(self):
        from lab1.memory_transfer import create_array, local_id_in_arr
        arr, d_arr = create_array(30)
        local_id_in_arr[1, 32](d_arr)
        arr = d_arr.copy_to_host()
        self.assertTrue(all(arr == range(30)))

    def test_global_id_in_arr_32_arr_1_block_32_threads(self):
        from lab1.memory_transfer import create_array, global_id_in_arr
        table_size = 320000
        arr, d_arr = create_array(table_size)
        threads_per_block = 1024
        blocks_per_grid = table_size + threads_per_block - 1 // threads_per_block

        global_id_in_arr[blocks_per_grid, threads_per_block](d_arr)
        arr = d_arr.copy_to_host()
        self.assertTrue(all(arr == range(table_size)))
