"""
    Given an array containing 0s and 1s, if you are allowed 
    to replace no more than `k` 0s with 1s, find the length 
    of the longest contiguous subarray having all 1s.

    Example 1:
    -------------
    Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
    Output: 6
    Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
    
    Example 2:
    ------------
    Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
    Output: 9
    Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""

from collections import defaultdict
import unittest


def longest_substring_ones_after_replacements(arr: list, K: int):
    start = 0
    hash_table = defaultdict(int)
    max_length = 0
    max_repeated_ones_count = 0

    for end in range(len(arr)):
        right_value = arr[end]
        hash_table[right_value] += 1

        if right_value == 1:
            max_repeated_ones_count += 1

        # shrinking process
        if (end + 1 - start - max_repeated_ones_count) > K:
            left_value = arr[start]
            hash_table[left_value] -= 1
            if hash_table[left_value] == 0:
                hash_table.pop(left_value)
            start += 1

            if left_value == 1:
                max_repeated_ones_count -= 1

        current_window_size = end + 1 - start
        if current_window_size > max_length:
            max_length = current_window_size

    return max_length


class TestCase(unittest.TestCase):
    def test_case1(self):
        return self.assertEqual(
            longest_substring_ones_after_replacements(
                [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2), 6
        )

    def test_case2(self):
        return self.assertEqual(
            longest_substring_ones_after_replacements(
                [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3), 9
        )


if __name__ == "__main__":
    unittest.main()
    # print(longest_substring_once_after_replacements(
    #     [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
