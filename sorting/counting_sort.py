"""
    ----------------------------------
    Counting Sort Algo Implementation
    ----------------------------------
"""

import unittest
import math


def counting_sort(arr: list[int]) -> None:
    """
    1. Non-comparition sorting algo.
    2. It requires the assumption about the input (max value or need to find the max among others), based on that we are creating counter arr, all having element value 0 initially.
    3. Need to iterate the input array and update the counter array index based on the input element value.
    4. Need to iterate the counter and update the original array for sorting.
    5. Major disadvantage is the elements required to be positive integer.
    """

    # Early return if the array is empty or size is 1
    n = len(arr)
    if n < 2:
        return
    
    # Find the max element
    max_element = -math.inf
    for i in range(n):
        if arr[i] > max_element:
            max_element = arr[i]

    # creating tempory counter array
    counter_arr = [0 for _ in range(max_element+1)]
    for i in arr:
        counter_arr[i] += 1

    # Updating original array 
    pointer = 0
    for j in range(len(counter_arr)):
        for _ in range(counter_arr[j]):
            arr[pointer] = j
            pointer += 1




class TestCase(unittest.TestCase):
    def test_unsorted_array(self) -> None:
        arr = [5,2,10,1,3]
        counting_sort(arr)
        self.assertEqual(arr, [1,2,3,5,10])

    def test_single_element_array(self) -> None:
        arr = [1]
        counting_sort(arr)
        self.assertEqual(arr, [1])

    def test_empty_array(self) -> None:
        arr = []
        counting_sort(arr)
        self.assertEqual(arr, [])

    def test_deplicate_elements_array(self) -> None:
        arr = [1,1,1]
        counting_sort(arr)
        self.assertEqual(arr, [1,1,1])

    def test_reverse_sorted_array(self) -> None:
        arr = [5,4,3,2,1,0]
        counting_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    def test_already_sorted_array(self) -> None:
        arr = [0,1,2,3,4,5]
        counting_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    

if __name__ == "__main__":
    unittest.main()