"""
Bubble sorting algorithm implementation

GFG: https://www.geeksforgeeks.org/problems/bubble-sort/1
"""
import unittest
from typing import TypeVar


T = TypeVar("T", int, float)

def bubble_sort_using_for_loop(arr: list[T]) -> None:
    n = len(arr)
    for i in range(n-1, 0, -1):
        is_sorted = True # for best case
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                is_sorted = False
        if is_sorted: return   

def bubble_sort_using_while_loop(arr: list[int]) -> None:
    n = len(arr)
    i = 0
    while (i < n-1):
        j = 0;
        while (j < n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            j += 1
        i += 1 


def bubble_sort_using_recursion(arr: list[int]) -> None:
    bubble_sort_using_recursion_helper(arr, len(arr), 0)

def bubble_sort_using_recursion_helper(arr: list[int], r: int, c: int) -> None:
    # Base condition
    if r <= 1:
        return
    
    if c < r-1:
        if arr[c] > arr[c+1]:
            arr[c], arr[c+1] = arr[c+1], arr[c]
        bubble_sort_using_recursion_helper(arr, r, c+1)
    else:
        bubble_sort_using_recursion_helper(arr, r-1, 0)
    


class TestCase(unittest.TestCase):
    def test_unsorted_array(self) -> None:
        arr = [5,2,10,1,3]
        bubble_sort_using_for_loop(arr)
        self.assertEqual(arr, [1,2,3,5,10])
        arr = [5,2,10,1,3]
        bubble_sort_using_while_loop(arr)
        self.assertEqual(arr, [1,2,3,5,10])
        arr = [5,2,10,1,3]
        bubble_sort_using_recursion(arr)
        self.assertEqual(arr, [1,2,3,5,10])

    def test_single_element_array(self) -> None:
        arr = [1]
        bubble_sort_using_for_loop(arr)
        self.assertEqual(arr, [1])
        arr = [1]
        bubble_sort_using_while_loop(arr)
        self.assertEqual(arr, [1])
        arr = [1]
        bubble_sort_using_recursion(arr)
        self.assertEqual(arr, [1])

    def test_empty_array(self) -> None:
        arr = []
        bubble_sort_using_for_loop(arr)
        self.assertEqual(arr, [])
        arr = []
        bubble_sort_using_while_loop(arr)
        self.assertEqual(arr, [])
        arr = []
        bubble_sort_using_recursion(arr)
        self.assertEqual(arr, [])

    def test_deplicate_elements_array(self) -> None:
        arr = [1,1,1]
        bubble_sort_using_for_loop(arr)
        self.assertEqual(arr, [1,1,1])
        arr = [1,1,1]
        bubble_sort_using_while_loop(arr)
        self.assertEqual(arr, [1,1,1])
        arr = [1,1,1]
        bubble_sort_using_recursion(arr)
        self.assertEqual(arr, [1,1,1])

    def test_reverse_sorted_array(self) -> None:
        arr = [5,4,3,2,1,0]
        bubble_sort_using_for_loop(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
        arr = [5,4,3,2,1,0]
        bubble_sort_using_while_loop(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
        arr = [5,4,3,2,1,0]
        bubble_sort_using_recursion(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    def test_already_sorted_array(self) -> None:
        arr = [0,1,2,3,4,5]
        bubble_sort_using_for_loop(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
        arr = [0,1,2,3,4,5]
        bubble_sort_using_while_loop(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
        arr = [0,1,2,3,4,5]
        bubble_sort_using_recursion(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
    

if __name__ == "__main__":
    unittest.main()