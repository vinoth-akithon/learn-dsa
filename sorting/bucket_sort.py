"""
Bucket Sort Implementation
"""


import unittest
import math
from counting_sort import counting_sort

def bucket_sort(arr: list[int]) -> None:
    """
    1. It's not comparition based sorting (But implesitely used comparition sorting to sort the elements inside the buckets)
    2. Need to find the total number of buckets (we can done of sqaure rooting the array length)
    3. need to iterate the array and insert element into a specific bucket.
    4. Sort all the buckets seperately
    5. Finally updating the input array by concatinating the buckets.
    """
    n = len(arr)
    if n < 2:
        return 
    total_buckets = int(math.sqrt(n))
    buckets = [[] for _ in range(total_buckets)]

    max_element = max(arr)
    for element in arr:
        bucket = int((element/max_element) * (total_buckets - 1))
        buckets[bucket].append(element)

    for bucket in buckets:
         counting_sort(bucket)

    pointer = 0
    for bucket in buckets:
        for element in bucket:
            arr[pointer] = element
            pointer += 1

class TestCase(unittest.TestCase):
    def test_unsorted_array(self) -> None:
        arr = [5,2,10,1,3]
        bucket_sort(arr)
        self.assertEqual(arr, [1,2,3,5,10])

    def test_single_element_array(self) -> None:
        arr = [1]
        bucket_sort(arr)
        self.assertEqual(arr, [1])

    def test_empty_array(self) -> None:
        arr = []
        bucket_sort(arr)
        self.assertEqual(arr, [])

    def test_deplicate_elements_array(self) -> None:
        arr = [1,1,1]
        bucket_sort(arr)
        self.assertEqual(arr, [1,1,1])

    def test_reverse_sorted_array(self) -> None:
        arr = [5,4,3,2,1,0]
        bucket_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    def test_already_sorted_array(self) -> None:
        arr = [0,1,2,3,4,5,6,7,8,9,10]
        bucket_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5,6,7,8,9,10])

    

if __name__ == "__main__":
    unittest.main()