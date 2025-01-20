import unittest


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
        bubble_sort_using_recursion(arr)
        self.assertEqual(arr, [1,2,3,5,10])

    def test_single_element_array(self) -> None:
        arr = [1]
        bubble_sort_using_recursion(arr)
        self.assertEqual(arr, [1])

    def test_empty_array(self) -> None:
        arr = []
        bubble_sort_using_recursion(arr)
        self.assertEqual(arr, [])

    def test_deplicate_elements_array(self) -> None:
        arr = [1,1,1]
        bubble_sort_using_recursion(arr)
        self.assertEqual(arr, [1,1,1])

    def test_reverse_sorted_array(self) -> None:
        arr = [5,4,3,2,1,0]
        bubble_sort_using_recursion(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    def test_already_sorted_array(self) -> None:
        arr = [0,1,2,3,4,5]
        bubble_sort_using_recursion(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    

if __name__ == "__main__":
    unittest.main()