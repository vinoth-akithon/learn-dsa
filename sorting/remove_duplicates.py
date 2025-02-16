import sys
import unittest
sys.path.append(".")

from sorting.merge_sort import merge_sort

def remove_duplicates(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    arr = merge_sort(arr)
    curr = arr[0]
    i = 1
    while i < len(arr):
        if arr[i] == curr:
            arr.pop(i)
        else:
            curr = arr[i]
            i += 1
    return arr


class TestCase(unittest.TestCase):
    def test_all_duplicates(self):
        arr = [2,3,2,5,3,5]
        self.assertEqual(remove_duplicates(arr), [2,3,5])  

    def test_one_duplicate(self):
        arr = [2,3,4,3]
        self.assertEqual(remove_duplicates(arr), [2,3,4])

    def test_non_duplicate(self):
        arr = [1,2,3,4,5]
        self.assertEqual(remove_duplicates(arr), [1,2,3,4,5])

    def test_empty_arr(self):
        arr = []
        self.assertEqual(remove_duplicates(arr), [])

    def test_single_elem(self):
        arr = [1]
        self.assertEqual(remove_duplicates(arr), [1])


if __name__ == "__main__":
    unittest.main()