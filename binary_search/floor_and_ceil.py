"""
- Given the sorted array of integers, we have tp find both ceil (smallest element which is >= target) and floor (greatest element which is <= target) value of the given target.

"""



def ceil(arr: list[int], t: int) -> int:
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



def solution(arr: list[int], t: int) -> int:
    """
        - Find both ceil and floor separately and return as list [floor, ceil]

        - Complexity Analysis:
            - Time -> O(2 log n) ~= O(log n)
            - Space -> O(1)
    """
    return [arr[floor(arr, t)], arr[ceil(arr, t)]]


if __name__ == "__main__":
    # arr = [3, 4, 4, 7, 8, 10];  t = 5
    arr = [3, 4, 4, 7, 8, 10]; t= 8
    print(solution(arr, t))