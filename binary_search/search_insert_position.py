"""
- Given an array of sorted integers and a target, we have to find the insert position.

"""


def insert_position(arr: list[int], t: int) -> int:
    """
    - Using Binary search ceiling approach.

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

        if arr[m] >= t:
            e = m-1
            ans = m
        else:
            s = m+1
    
    return ans


if __name__ == "__main__":
    arr = [1,2,4,7]; t = 6
    # arr = [1,2,4,7]; t = 2
    # arr =  []; t = 1
    print(insert_position(arr, t))
