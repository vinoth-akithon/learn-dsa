"""
Given an array of sorted integers and a target, we have to find the fist and last occurrences of the target value.
"""


def ceil(arr: list[int], t: int) -> int:
    """
        - Using binary search

        - Complexity Analysis:
            - Time -> O(log n)
            - Space -> O(1)
    """
    n = len(arr)
    s = 0
    e = n-1
    ans = n

    while (s <= e):
        m = s + (e-s)//2

        if arr[m] >= t:
            e = m -1
            if arr[m] == t:
                ans = m
        else:
            s = m + 1
        
    return ans

def floor(arr: list[int], t: int) -> int:
    """
        - Using binary search

        - Complexity Analysis:
            - Time -> O(log n)
            - Space -> O(1)
    """
    n = len(arr)
    s = 0
    e = n-1
    ans = -1

    while (s <= e):
        m = s + (e-s)//2

        if arr[m] <= t:
            s = m + 1
            if arr[m] == t:
                ans = m
        else:
            e = m -1
        
    return ans


def solution(arr: list[int], t: int) -> int:
    """
        - find the lower bound (ceil) as it is a first occurrence.
        - Find the upper bound (floor) as it is a last occurrence.
        - Finally return both indices.

        - Complexity Analysis:
            - Time -> O(2 log n) ~= O(log n)
            - Space -> O(1)
    """

    first_occur = ceil(arr, t)
    if first_occur != len(arr):
        last_occur = floor(arr, t)
        return [first_occur, last_occur]
    else:
        return [-1, -1]


if __name__ == "__main__":
    arr = [3, 4, 13, 13, 13, 20, 40]; t=13
    # arr = [3, 4, 13, 13, 13, 20, 40]; t=60
    # arr = [5,7,7,8,8,10]; t = 8
    print(solution(arr, t))

