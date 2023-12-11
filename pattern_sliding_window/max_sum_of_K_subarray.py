"""
    Given an array of positive numbers and a positive number K,
    find the maximum sum of any contiguous subarray of size K.

    Example1:
        Input: [2, 1, 5, 1, 3, 2], K=3 
        Output: 9 
        Explanation: Subarray with maximum sum is [5, 1, 3].

    Example2:
        Input: [2, 3, 4, 1, 5], K=2 
        Output: 7
        Explanation: Subarray with maximum sum is [3, 4].

    Time Complexity: O(N)
    Space Comlexity: O(1)

"""
import unittest
import timeit


def max_sub_array_of_size_k1(arr: list[int], K: int) -> int:
    window_sum = 0
    window_start = 0
    result = []  # O(N) space

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= K-1:
            result.append(window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max(result)


def max_sub_array_of_size_k2(arr: list[int], K: int) -> int:
    window_sum = 0
    max_sum = float("-inf")  # O(1) space

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= K-1:
            if window_sum > max_sum:
                max_sum = window_sum
            window_sum -= arr[window_end+1-K]
    return max_sum


class TestMaxSum(unittest.TestCase):
    def test_case1(self):
        return self.assertEqual(
            max_sub_array_of_size_k2([2, 1, 5, 1, 3, 2], 3), 9)

    def test_case2(self):
        return self.assertEqual(
            max_sub_array_of_size_k2([2, 3, 4, 1, 5], 2), 7)


if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    K = 3
    unittest.main()

    # print(timeit.timeit(
    #     "max_sub_array_of_size_k1(arr, K)",
    #     setup="from __main__ import max_sub_array_of_size_k1, arr, K"))
    # print(timeit.timeit(
    #     "max_sub_array_of_size_k2(arr, K)",
    #     setup="from __main__ import max_sub_array_of_size_k2, arr, K"))
