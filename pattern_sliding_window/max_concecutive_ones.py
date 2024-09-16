"""
    Given a binary array nums, return the maximum number 
    of consecutive 1's in the array.

    Example 1:
    ------------
    Input: nums = [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s. 
                The maximum number of consecutive 1s is 3.
    
    Example 2:
    ----------
    Input: nums = [1,0,1,1,0,1]
    Output: 2
"""

from collections import defaultdict


def find_max_consecutive_ones(nums: list[int]) -> int:
    start = 0
    max_repeated_ones = 0
    max_length = 0

    for end in range(len(nums)):
        right_item = nums[end]
        if right_item == 1:
            max_repeated_ones += 1

        # shrinking process
        while (end + 1 - start) != max_repeated_ones:
            left_item = nums[start]
            start += 1
            if left_item == 1:
                max_repeated_ones -= 1

        if max_repeated_ones > max_length:
            max_length = max_repeated_ones
    return max_length


if __name__ == "__main__":
    print(find_max_consecutive_ones([1, 1, 0, 1, 1, 1]))
    # print(find_max_consecutive_ones([0]))
    # print(find_max_consecutive_ones([1, 0, 1, 1, 0, 1]))
