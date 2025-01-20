"""
Selection Sort Implementation

The name selction sort implies that for each pass,
we are selecting the maxlimum value from the array 
and move it into right position.

GFG: https://www.geeksforgeeks.org/problems/selection-sort/1
"""

import unittest
from typing import TypeVar

T = TypeVar("T", int, float)

# def selection_sort(arr: list[int]) -> None:
#     selection_sort_helper(arr, len(arr), len(arr), 1, 0)


# def selection_sort_helper(arr: list[int], size: int, r: int, c: int, current_min_index: int) -> None:
#     # Base condition
#     if r == 0:
#         return
    
#     if c < size:
#         if arr[c] < arr[current_min_index]:
#             current_min_index = c;
#         selection_sort_helper(arr, size, r, c+1, current_min_index)
#     else:
#         arr[current_min_index], arr[size-r] = arr[size-r], arr[current_min_index]
#         temp = size - (r-1) + 1
#         selection_sort_helper(arr, size, r-1, temp, size-r+1)
        
        
# arr = []
# selection_sort(arr)
# print(arr)

def selection_sort(arr: list[int]) -> None:
    """Placing the smallest element at right position."""
    n = len(arr)
    for i in range(n-1):
        current_min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[current_min_index]:
                current_min_index = j;
        
        arr[current_min_index], arr[i] = arr[i], arr[current_min_index]

def selection_sort_using_for_loop(arr: list[int]) -> None:
    """Placing the largest element at right position."""
    n = len(arr)
    for i in range(n-1, 0, -1):
        current_max_index = 0;
        for j in range(1, i+1):
            if arr[j] > arr[current_max_index]:
                current_max_index = j;
        arr[current_max_index], arr[i] = arr[i], arr[current_max_index]



def selection_sort_using_while_loop(arr: list[int]) -> None:
    n = len(arr)
    i = 0;
    while i < n-1:
        j = 0;
        current_max_index = 0;
        while j < n-i:
            if arr[j] > arr[current_max_index]:
                current_max_index = j;
            j += 1;
        arr[current_max_index], arr[j-1] = arr[j-1], arr[current_max_index]
        i += 1;



def selection_sort_using_recursion(arr: list[int]) -> None:
    selection_sort_using_recursion_helper(arr, len(arr), 1, 0)

def selection_sort_using_recursion_helper(arr: list[int], r: int, c: int, current_max_index: int):
    # Base condition
    if r <= 1:
        return 
    
    if c < r:
        if arr[c] > arr[current_max_index]:
            current_max_index = c;
        selection_sort_using_recursion_helper(arr, r, c+1, current_max_index)
    else:
        arr[current_max_index], arr[c-1] = arr[c-1], arr[current_max_index]
        selection_sort_using_recursion_helper(arr, r-1, 1, 0)



class TestCase(unittest.TestCase):
    def test_unsorted_array(self) -> None:
        arr = [5,2,10,1,3]
        selection_sort(arr)
        self.assertEqual(arr, [1,2,3,5,10])
        arr = [5,2,10,1,3]
        selection_sort_using_for_loop(arr)
        self.assertEqual(arr, [1,2,3,5,10])
        arr = [5,2,10,1,3]
        selection_sort_using_while_loop(arr)
        self.assertEqual(arr, [1,2,3,5,10])
        arr = [5,2,10,1,3]
        selection_sort_using_recursion(arr)
        self.assertEqual(arr, [1,2,3,5,10])

    def test_single_element_array(self) -> None:
        arr = [1]
        selection_sort(arr)
        self.assertEqual(arr, [1])
        arr = [1]
        selection_sort_using_for_loop(arr)
        self.assertEqual(arr, [1])
        arr = [1]
        selection_sort_using_while_loop(arr)
        self.assertEqual(arr, [1])
        arr = [1]
        selection_sort_using_recursion(arr)
        self.assertEqual(arr, [1])

    def test_empty_array(self) -> None:
        arr = []
        selection_sort(arr)
        self.assertEqual(arr, [])
        arr = []
        selection_sort_using_for_loop(arr)
        self.assertEqual(arr, [])
        arr = []
        selection_sort_using_while_loop(arr)
        self.assertEqual(arr, [])
        arr = []
        selection_sort_using_recursion(arr)
        self.assertEqual(arr, [])

    def test_deplicate_elements_array(self) -> None:
        arr = [1,1,1]
        selection_sort(arr)
        self.assertEqual(arr, [1,1,1])
        arr = [1,1,1]
        selection_sort_using_for_loop(arr)
        self.assertEqual(arr, [1,1,1])
        arr = [1,1,1]
        selection_sort_using_while_loop(arr)
        self.assertEqual(arr, [1,1,1])
        arr = [1,1,1]
        selection_sort_using_recursion(arr)
        self.assertEqual(arr, [1,1,1])

    def test_reverse_sorted_array(self) -> None:
        arr = [5,4,3,2,1,0]
        selection_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
        arr = [5,4,3,2,1,0]
        selection_sort_using_for_loop(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
        arr = [5,4,3,2,1,0]
        selection_sort_using_while_loop(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
        arr = [5,4,3,2,1,0]
        selection_sort_using_recursion(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    def test_already_sorted_array(self) -> None:
        arr = [0,1,2,3,4,5]
        selection_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
        arr = [0,1,2,3,4,5]
        selection_sort_using_for_loop(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
        arr = [0,1,2,3,4,5]
        selection_sort_using_while_loop(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])
        arr = [0,1,2,3,4,5]
        selection_sort_using_recursion(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    

if __name__ == "__main__":
    unittest.main()

     