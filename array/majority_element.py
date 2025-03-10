"""
    Majority Element
    Link: https://leetcode.com/problems/majority-element/
"""

import math


def majority_element(arr: list[int]) -> int:
    """
        - Keeping majority element and frequency pointer
        - Time -> O(n)
        - Space -> O(1)
    """
    n = len(arr)
    e = arr[0]
    f = 1
    i = 1
    while (i < n):
        if arr[i] == e:
            f += 1
        elif f == 1:
            e = arr[i]
        else:
            f -= 1
        i += 1
    return e

if __name__ == "__main__":
    arr = [3,2,3]
    # arr = [2,2,1,1,1,2,2]
    # arr = [6,5,5]
    print(majority_element(arr))