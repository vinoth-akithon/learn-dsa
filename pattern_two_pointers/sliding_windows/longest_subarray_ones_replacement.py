"""
    Longest subarray of concecutive 1's after replacement of 0's. variation of longest repeating characters replacement

    LC Link: https://leetcode.com/problems/max-consecutive-ones-iii/description/  

"""

import collections

def longest_subarray(arr: list[int], k: int) -> int:
    n = len(arr)
    l = 0
    zeros_count = 0
    max_window = 0

    for r in range(n):
        right_elem = arr[r]
        if right_elem == 0:
            zeros_count += 1

        # Check valid window
        while zeros_count > k:
            left_elem = arr[l]
            if left_elem == 0:
                zeros_count -= 1
            l += 1


        current_window = r - l + 1
        max_window = max(max_window, current_window)

    return max_window

    


if __name__ == "__main__":
    # arr = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]; k=2
    # arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]; k=3
    arr = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]; k=3
    print(longest_subarray(arr, k))