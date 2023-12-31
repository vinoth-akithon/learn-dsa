"""
    Given an array of positive numbers and a positive number S, 
    find the length of the smallest contiguous subarray whose sum
    is greater than or equal to S. Return 0, if no such subarray exists.

    Example 1:
        Input: [2, 1, 5, 2, 3, 2], S=7 
        Output: 2
        Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

    Example 2:
        Input: [2, 1, 5, 2, 8], S=7 
        Output: 1
        Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

    Example 3:
        Input: [3, 4, 1, 1, 6], S=8 
        Output: 3
        Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].


    Time Complexity: O(N + N) = O(N)
    Space Comlexity: O(1)

"""


import unittest
import timeit


def smallest_subarray_with_given_sum(arr, S):
    window_start = 0
    window_sum = 0
    smallest_window_size = float("inf")

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= S:
            current_window_size = (window_end+1-window_start)
            if current_window_size < smallest_window_size:
                smallest_window_size = current_window_size
            window_sum -= arr[window_start]
            window_start += 1
    return smallest_window_size if smallest_window_size != float("inf") else 0


class TestSmallestSubarrayWithGivenSum(unittest.TestCase):
    def test_case1(self):
        return self.assertEqual(smallest_subarray_with_given_sum([2, 1, 5, 2, 3, 2], 7), 2)

    def test_case2(self):
        return self.assertEqual(smallest_subarray_with_given_sum([2, 1, 5, 2, 8], 7), 1)

    def test_case3(self):
        return self.assertEqual(smallest_subarray_with_given_sum([3, 4, 1, 1, 6], 8), 3)


if __name__ == "__main__":
    arr = [2, 1, 5, 2, 3, 2]
    S = 7
    # print(smallest_subarray_with_given_sum(arr, S))
    unittest.main()

    # print(timeit.timeit("smallest_subarray_with_given_sum(arr, S)",
    #       setup="from __main__ import smallest_subarray_with_given_sum, arr, S"))
