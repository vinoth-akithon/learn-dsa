"""
Merge Sort Implementaion
"""

import unittest
from typing import TypeVar

T = TypeVar("T", int, float)
    

def merge(left_arr: list[T], right_arr: list[T], arr) -> list[T]:
    i = j = k = 0
    while (i < len(left_arr) and j < len(right_arr)):
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while (i < len(left_arr)):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while (j < len(right_arr)):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    return arr


def merge_sort(arr: list[T]) -> list[T]:
    n = len(arr)
    # base condition for recursion
    if n < 2:
        return arr

    # devide the array into half and sort them seperately
    mid = n//2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])

    # merge the two sorted subarray
    return merge(left_arr, right_arr, arr)



class TestCase(unittest.TestCase):
    def test_unsorted_array(self) -> None:
        arr = [5,2,10,1,3]
        merge_sort(arr)
        self.assertEqual(arr, [1,2,3,5,10])

    def test_single_element_array(self) -> None:
        arr = [1]
        merge_sort(arr)
        self.assertEqual(arr, [1])

    def test_empty_array(self) -> None:
        arr = []
        merge_sort(arr)
        self.assertEqual(arr, [])

    def test_deplicate_elements_array(self) -> None:
        arr = [1,1,1]
        merge_sort(arr)
        self.assertEqual(arr, [1,1,1])

    def test_reverse_sorted_array(self) -> None:
        arr = [5,4,3,2,1,0]
        merge_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    def test_already_sorted_array(self) -> None:
        arr = [0,1,2,3,4,5]
        merge_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    

if __name__ == "__main__":
    unittest.main()