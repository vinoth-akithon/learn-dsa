import unittest
from typing import TypeVar

T = TypeVar("T", int, float)


def shell_sort(arr: list[T]) -> None:
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n, gap):
            temp = arr[i]
            j = i
            while (j >= gap and arr[j-gap] > temp):
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2

class TestCase(unittest.TestCase):
    def test_unsorted_array(self) -> None:
        arr = [5,2,10,1,3]
        shell_sort(arr)
        self.assertEqual(arr, [1,2,3,5,10])

    def test_single_element_array(self) -> None:
        arr = [1]
        shell_sort(arr)
        self.assertEqual(arr, [1])

    def test_empty_array(self) -> None:
        arr = []
        shell_sort(arr)
        self.assertEqual(arr, [])

    def test_deplicate_elements_array(self) -> None:
        arr = [1,1,1]
        shell_sort(arr)
        self.assertEqual(arr, [1,1,1])

    def test_reverse_sorted_array(self) -> None:
        arr = [5,4,3,2,1,0]
        shell_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    def test_already_sorted_array(self) -> None:
        arr = [0,1,2,3,4,5]
        shell_sort(arr)
        self.assertEqual(arr, [0,1,2,3,4,5])

    



if __name__ == "__main__":
    unittest.main()