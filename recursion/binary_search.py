from typing import Annotated
import unittest

def binary_search_recursive(arr: list[int], target) -> Annotated[int, "Returns the index of the target or else returns -1"]:
    return __binary_search_recursive(arr, target, 0, len(arr)-1)

def __binary_search_recursive(arr: list[int], target: int, start: int, end: int) -> int:
    if start > end:
        return -1
    
    mid = start + (end-start)//2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return __binary_search_recursive(arr, target, mid+1, end)
    return __binary_search_recursive(arr, target, start, mid-1)


class TestCase(unittest.TestCase):
    def test_empty_array(self):
        arr = []
        target = 60
        self.assertEqual(binary_search_recursive(arr, target), -1)

    def test_array_with_target_not_present(self):
        arr = [10]
        target = 60
        self.assertEqual(binary_search_recursive(arr, target), -1)

    def test_array_with_target_present(self):
        arr = [10, 20, 30, 40, 50, 60, 70]
        target = 60
        self.assertEqual(binary_search_recursive(arr, target), 5)
        target = 10
        self.assertEqual(binary_search_recursive(arr, target), 0)
        target = 40
        self.assertEqual(binary_search_recursive(arr, target), 3)



if __name__ == "__main__":
    # arr = [10, 20, 30, 40, 50, 60, 70]
    # target = 100
    # print(binary_search_recursive(arr, target))
    unittest.main()