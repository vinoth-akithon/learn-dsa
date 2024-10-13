"""
Insertion sort implementation
"""

import unittest
from typing import TypeVar

T = TypeVar("T", int, float)


def insertion_sort(arr: list[T]) -> None:
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i

        while (j > 0 and arr[j-1] > temp):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp



class TestCase(unittest.TestCase):
    def test_unsorted_array(self) -> None:
        arr = [5,2,10,1,3]
        insertion_sort(arr)
        self.assertEqual(arr, [1,2,3,5,10])

    def test_single_element_array(self) -> None:
        arr = [1]
        insertion_sort(arr)
        self.assertEqual(arr, [1])

    def test_empty_array(self) -> None:
        arr = []
        insertion_sort(arr)
        self.assertEqual(arr, [])

    def test_deplicate_elements_array(self) -> None:
        arr = [1,1,1]
        insertion_sort(arr)
        self.assertEqual(arr, [1,1,1])

    def test_reverse_sorted_array(self) -> None:
        arr = [5,4,3,2,1,0]
        insertion_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    def test_already_sorted_array(self) -> None:
        arr = [0,1,2,3,4,5]
        insertion_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    

if __name__ == "__main__":
    unittest.main()