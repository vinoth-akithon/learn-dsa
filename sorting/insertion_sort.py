"""
Insertion sort implementation.

GFG: https://www.geeksforgeeks.org/problems/insertion-sort/1
"""

import unittest
from typing import TypeVar

T = TypeVar("T", int, float)


def insertion_sort(arr: list[T]) -> None:
    n = len(arr)
    for i in range(1, n):
        j = i-1
        temp = arr[i]
        while (j >= 0 and temp < arr[j]):
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1;
        arr[j+1] = temp


def insertion_sort_recursive(arr: list[int]) -> None:
    if len(arr) < 2:
        return 
    insertion_sort_recursive_helper(arr, 0, 1, arr[1])

def insertion_sort_recursive_helper(arr, j, i, value) -> None:
    if (j >= 0 and value < arr[j]):
        arr[j], arr[j+1] = arr[j+1], arr[j]
        insertion_sort_recursive_helper(arr, j-1, i, value)
    else:
        arr[j+1] = value
        if i+1 == len(arr):
            return 
        insertion_sort_recursive_helper(arr, i, i+1, arr[i+1])


def insertion_sort_using_binary_search(arr: list[int]) -> None:
    n = len(arr)
    for i in range(1, n):
        j = i-1
        temp = arr[i]
        pos = binary_search(arr, temp, 0, j)
        while j >= pos:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
        arr[j+1] = temp

def binary_search(arr: list[int], target: int, start: int, end: int) -> int:
    if start > end:
        return start
    
    mid = (start + end) // 2
    if target < arr[mid]:
        return binary_search(arr, target, start, mid-1)
    else:
        return binary_search(arr, target, mid+1, end)



class TestCase(unittest.TestCase):
    def test_unsorted_array(self) -> None:
        arr = [5,2,10,1,3]
        insertion_sort(arr)
        self.assertEqual(arr, [1,2,3,5,10])
        arr = [5,2,10,1,3]
        insertion_sort_recursive(arr)
        self.assertEqual(arr, [1,2,3,5,10])
        arr = [5,2,10,1,3]
        insertion_sort_recursive(arr)
        self.assertEqual(arr, [1,2,3,5,10])
        arr = [5,2,10,1,3]
        insertion_sort_using_binary_search(arr)
        self.assertEqual(arr, [1,2,3,5,10])

    def test_single_element_array(self) -> None:
        arr = [1]
        insertion_sort(arr)
        self.assertEqual(arr, [1])
        arr = [1]
        insertion_sort_recursive(arr)
        self.assertEqual(arr, [1])
        arr = [1]
        insertion_sort_recursive(arr)
        self.assertEqual(arr, [1])
        arr = [1]
        insertion_sort_using_binary_search(arr)
        self.assertEqual(arr, [1])

    def test_empty_array(self) -> None:
        arr = []
        insertion_sort(arr)
        self.assertEqual(arr, [])
        arr = []
        insertion_sort_recursive(arr)
        self.assertEqual(arr, [])
        arr = []
        insertion_sort_recursive(arr)
        self.assertEqual(arr, [])
        arr = []
        insertion_sort_using_binary_search(arr)
        self.assertEqual(arr, [])

    def test_deplicate_elements_array(self) -> None:
        arr = [1,1,1]
        insertion_sort(arr)
        self.assertEqual(arr, [1,1,1])
        arr = [1,1,1]
        insertion_sort_recursive(arr)
        self.assertEqual(arr, [1,1,1])
        arr = [1,1,1]
        insertion_sort_recursive(arr)
        self.assertEqual(arr, [1,1,1])
        arr = [1,1,1]
        insertion_sort_using_binary_search(arr)
        self.assertEqual(arr, [1,1,1])

    def test_reverse_sorted_array(self) -> None:
        arr = [5,4,3,2,1,0]
        insertion_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
        arr = [5,4,3,2,1,0]
        insertion_sort_recursive(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
        arr = [5,4,3,2,1,0]
        insertion_sort_recursive(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
        arr = [5,4,3,2,1,0]
        insertion_sort_using_binary_search(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    def test_already_sorted_array(self) -> None:
        arr = [0,1,2,3,4,5]
        insertion_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
        arr = [0,1,2,3,4,5]
        insertion_sort_recursive(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
        arr = [0,1,2,3,4,5]
        insertion_sort_recursive(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
        arr = [0,1,2,3,4,5]
        insertion_sort_using_binary_search(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    

if __name__ == "__main__":
    unittest.main()