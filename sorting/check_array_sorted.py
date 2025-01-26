"""
    Check whether the array is sorted or not
    GFG: https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1
"""

import unittest

def is_array_sorted(arr: list[int]) -> bool:
    """ Single Traversal involves
        Time -> O(N)
        Space -> O(1)
    """
    n = len(arr)
    for i in range(1, n-1):
        if arr[i-1] > arr[i]:
            return False
    return True

# def arraySortedOrNot(self, arr) -> bool:
#     n = len(arr)
#     i = 1
#     while (i < n):
#         if arr[i-1] > arr[i]:
#             return False
#         i += 1
#     return True
    
def is_array_sorted_recursive(arr) -> bool:
    """ Recursive Approach
        Time -> O(N)
        Space -> O(1)
    """
    return is_array_sorted_recursive_helper(arr, 0)

def is_array_sorted_recursive_helper(arr, p) -> bool:
    # Base condition
    if p >= len(arr)-1:
        return True
    return (arr[p] <= arr[p+1]) and is_array_sorted_recursive_helper(arr, p+1)


class TestCase(unittest.TestCase):
    def test_unsorted(self):
        arr = [10, 8, 3, 5, 12]
        self.assertEqual(is_array_sorted_recursive(arr), False)
        self.assertEqual(is_array_sorted(arr), False)

    def test_accending_sorted(self):
        arr = [10, 12, 30, 45, 100]
        self.assertEqual(is_array_sorted_recursive(arr), True)
        self.assertEqual(is_array_sorted(arr), True)

    def test_decending_sorted(self):
        arr = [10, 8, 6, 4, 2]
        self.assertEqual(is_array_sorted_recursive(arr), False)
        self.assertEqual(is_array_sorted(arr), False)

    def test_empty_array(self):
        arr = []
        self.assertEqual(is_array_sorted_recursive(arr), True)
        self.assertEqual(is_array_sorted(arr), True)

    def test_single_element_array(self):
        arr = [10]
        self.assertEqual(is_array_sorted_recursive(arr), True)
        self.assertEqual(is_array_sorted(arr), True)


if __name__ == "__main__":
    unittest.main()