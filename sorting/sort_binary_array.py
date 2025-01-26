"""
    Segregate 0s and 1s
    GFG: https://www.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1
"""


import unittest


def sort_binary_arr_naive_approach(arr):
    """ Two Traversal involves
        Time -> O(2N) ~= O(n)
        Space -> O(1)
    """
    n = len(arr)
    zeros_count = 0
    for i in range(n):
        if arr[i] == 0:
            zeros_count += 1
    for j in range(zeros_count):
        arr[j] = 0
    for k in range(zeros_count, n):
        arr[k] = 1


def sort_binary_arr_two_poiners(arr):
    n = len(arr)
    s = 0
    e = n-1
    while s < e:
        while s < n and arr[s] == 0:
            s += 1
        while e >= 0 and arr[e] == 1:
            e -= 1
        if s < e:
            arr[s], arr[e] = arr[e], arr[s]
            s += 1
            e -= 1



def sort_binary_arr(arr):
    """ Single Traversal Involves
        Time -> O(N)
        Space -> O(1)
    """
    n = len(arr)
    b = -1
    for i in range(n):
        if arr[i] == 0:
            b += 1
            if b != i:
                arr[b], arr[i] = arr[i], arr[b]


# def partition_logic(arr):
#     n = len(arr)
#     pivot = arr[n-1]
#     boundary = 0
#     for i in range(n):
#         if arr[i] <= pivot:
#             arr[boundary], arr[i] = arr[i], arr[boundary]
#             boundary += 1
#     return boundary-1, arr[boundary-1]


class TestCase(unittest.TestCase):
    def test_unsorted(self):
        arr = [0,1,1,0,0,1]
        sort_binary_arr_naive_approach(arr)
        self.assertEqual(arr, [0, 0, 0, 1, 1, 1])
        arr = [0,1,1,0,0,1]
        sort_binary_arr(arr)
        self.assertEqual(arr, [0, 0, 0, 1, 1, 1])
        arr = [0,1,1,0,0,1]
        sort_binary_arr_two_poiners(arr)
        self.assertEqual(arr, [0, 0, 0, 1, 1, 1])
    
    def test_sorted(self):
        arr = [0,0, 1, 1]
        sort_binary_arr_naive_approach(arr)
        self.assertEqual(arr, [0, 0, 1, 1])
        arr = [0,0, 1, 1]
        sort_binary_arr(arr)
        self.assertEqual(arr, [0, 0, 1, 1])
        arr = [0,0, 1, 1]
        sort_binary_arr_two_poiners(arr)
        self.assertEqual(arr, [0, 0, 1, 1])

    def test_reverse_sorted(self):
        arr = [1,1,1,0, 0]
        sort_binary_arr_naive_approach(arr)
        self.assertEqual(arr, [0,0,1,1,1])
        arr = [1,1,1,0, 0]
        sort_binary_arr(arr)
        self.assertEqual(arr, [0,0,1,1,1])
        arr = [1,1,1,0, 0]
        sort_binary_arr_two_poiners(arr)
        self.assertEqual(arr, [0,0,1,1,1])

    def test_only_zeros_array(self):
        arr = [0, 0, 0]
        sort_binary_arr_naive_approach(arr)
        self.assertEqual(arr, [0,0,0])
        arr = [0, 0, 0]
        sort_binary_arr(arr)
        self.assertEqual(arr, [0,0,0])
        arr = [0, 0, 0]
        sort_binary_arr_two_poiners(arr)
        self.assertEqual(arr, [0,0,0])

    def test_only_ones_array(self):
        arr = [1,1,1,1]
        sort_binary_arr_naive_approach(arr)
        self.assertEqual(arr, [1,1,1,1])
        arr = [1,1,1,1]
        sort_binary_arr(arr)
        self.assertEqual(arr, [1,1,1,1])
        arr = [1,1,1,1]
        sort_binary_arr_two_poiners(arr)
        self.assertEqual(arr, [1,1,1,1])

    def test_empty_array(self):
        arr = []
        sort_binary_arr_naive_approach(arr)
        self.assertEqual(arr, [])
        arr = []
        sort_binary_arr(arr)
        self.assertEqual(arr, [])
        arr = []
        sort_binary_arr_two_poiners(arr)
        self.assertEqual(arr, [])
    
    def test_one_element_array(self):
        arr = [1]
        sort_binary_arr_naive_approach(arr)
        self.assertEqual(arr, [1])
        arr = [1]
        sort_binary_arr(arr)
        self.assertEqual(arr, [1])
        arr = [1]
        sort_binary_arr_two_poiners(arr)
        self.assertEqual(arr, [1])


if __name__ == "__main__":
    unittest.main()
    # arr = [0,0,1,1]
    # sort_binary_arr_two_poiners(arr)