"""
Given an array of integers in sorting order, we have to find the floor of the target (Upper bound). which means an element
which is previous to lesser than or equal to target.
"""


def floor(arr: list[int], t: int) -> int:
    """
        - Using Binary search.

        - Complexity Analysis:
            - Time -> O(log n)
            - Space -> O(1)
    """
    n = len(arr)
    s = 0
    e = n-1

    while (s <= e):
        m = s + (e-s)//2

        if arr[m] <= t:
            s = m + 1
        else:
            e = m -1
    
    return e


if __name__ == "__main__":
    arr = [1,2,3,5,17,18]; t = 0
    # arr = [1, 1, 4, 4, 4, 4, 10]; t = 4
    print(floor(arr, t))