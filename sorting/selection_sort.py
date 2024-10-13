"""
Selection Sort Implementation

The name selction sort implies that for each pass,
we are selecting the maxlimum value from the array 
and move it into right position.
"""

import unittest
from typing import TypeVar

T = TypeVar("T", int, float)

def selection_sort(arr: list[T]) -> None:
    n = len(arr)
    for i in range(n-1, 0, -1):
        max_value_index = 0
        for j in range(1, i+1):
            if arr[j] > arr[max_value_index]:
                max_value_index = j
        arr[max_value_index], arr[i] = arr[i], arr[max_value_index]


class TestCase(unittest.TestCase):
    def test_unsorted_array(self) -> None:
        arr = [5,2,10,1,3]
        selection_sort(arr)
        self.assertEqual(arr, [1,2,3,5,10])

    def test_single_element_array(self) -> None:
        arr = [1]
        selection_sort(arr)
        self.assertEqual(arr, [1])

    def test_empty_array(self) -> None:
        arr = []
        selection_sort(arr)
        self.assertEqual(arr, [])

    def test_deplicate_elements_array(self) -> None:
        arr = [1,1,1]
        selection_sort(arr)
        self.assertEqual(arr, [1,1,1])

    def test_reverse_sorted_array(self) -> None:
        arr = [5,4,3,2,1,0]
        selection_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    def test_already_sorted_array(self) -> None:
        arr = [0,1,2,3,4,5]
        selection_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    

if __name__ == "__main__":
    unittest.main()

     