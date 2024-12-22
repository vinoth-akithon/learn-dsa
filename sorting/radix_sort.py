import unittest

def radix_sort(arr: list[int]):
    """
    1. Radix sort is a non-comparition sorting algorithm.
    2. It requires some assumption about input like couting/bucket sort algo and all the elements in the input should be `d` digits.
    3. First sort the element based on the least significant digit by creating a buckets and distributing elements into buckets.
    4. Iterate the bucket and update the input array.
    5. Move on to the next least significant digit and do until more significant digit.
    """
    n = len(arr)
    if n < 2:
        return 
    
    radix = 10
    base = 1
    does_digit_avail = True

    while does_digit_avail:
        buckets = [[] for _ in range(radix)]
        
        for element in arr:
            temp = int(element/base)
            bucket = temp%radix
            buckets[bucket].append(element)
            if temp <= 0:
                does_digit_avail = False

        pointer = 0
        for bucket in buckets:
            for element in bucket:
                arr[pointer] = element
                pointer += 1

        base *= 10



class TestCase(unittest.TestCase):
    def test_unsorted_array(self) -> None:
        arr = [5,2,10,1,3]
        radix_sort(arr)
        self.assertEqual(arr, [1,2,3,5,10])

    def test_single_element_array(self) -> None:
        arr = [1]
        radix_sort(arr)
        self.assertEqual(arr, [1])

    def test_empty_array(self) -> None:
        arr = []
        radix_sort(arr)
        self.assertEqual(arr, [])

    def test_deplicate_elements_array(self) -> None:
        arr = [1,1,1]
        radix_sort(arr)
        self.assertEqual(arr, [1,1,1])

    def test_reverse_sorted_array(self) -> None:
        arr = [5,4,3,2,1,0]
        radix_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    def test_already_sorted_array(self) -> None:
        arr = [521, 453, 354, 360, 245, 278, 600, 121]
        radix_sort(arr)
        self.assertEqual(arr, [121, 245, 278, 354, 360, 453, 521, 600])

    

if __name__ == "__main__":
    unittest.main()