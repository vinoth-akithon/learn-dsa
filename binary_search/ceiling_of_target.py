"""
Given an array of integers in sorting order, we have to find the ceiling of the target (Lower bound). which means an element
which is next greater or equal to target.
"""


def ceiling(arr: list[int], t: int) -> int:
    """
        - Using Binary search.

        - Complexity Analysis:
            - Time -> O(log n)
            - Space -> O(1)
    """
    n = len(arr)
    s = 0
    e = n-1

    if t > arr[-1]:
        return -1

    while (s <= e):
        m = s + (e-s)//2

        if arr[m] >= t:
            e = m-1
        else:
            s = m+1
    
    return s


if __name__ == "__main__":
    arr = [1,2,3,5,17,18]; t = 18
    # arr = [1, 1, 4, 4, 4, 4, 10]; t = 4
    print(ceiling(arr, t))