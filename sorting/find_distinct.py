import sys
sys.path.append(".")
from merge_sort import merge_sort
import unittest

def find_distinct(arr: list[int]) -> int:
    n = len(arr)
    if not n:
        return -1
    arr = merge_sort(arr)
    curr = arr[0]
    count = 1
    for i in range(1, n):
        if arr[i] == curr:
            count += 1
        elif count > 1:
            curr = arr[i]
            count = 1
        else:
            break
    return -1 if count > 1 else curr
            
    
class TestCase(unittest.TestCase):
    def test_one_unique_elem(self):
        arr = [1,2,5,2,3,5,7,7,1]
        self.assertEqual(find_distinct(arr), 3)

    def test_empty_arr(self):
        arr = []
        self.assertEqual(find_distinct(arr), -1)
    
    def test_single_elem(self):
        arr = [3]
        self.assertEqual(find_distinct(arr), 3)

    def test_non_distinct(self):
        arr = [2,3,2,3]
        self.assertEqual(find_distinct(arr), -1)
    
    def test_non_distict(self):
        arr = [3,3,3]
        self.assertEqual(find_distinct(arr), -1)
    


if __name__ == "__main__":
    unittest.main()