"""
Given the array of integers with non duplicates and sorted in acceding order with unknown rotated position.

The minimum is always in the UNSORTED half.

[4, 5, 6, 7, 1, 2, 3]
              ^
           minimum

If arr[mid] > arr[hi]: minimum is in RIGHT half → lo = mid + 1
If arr[mid] < arr[hi]: minimum is in LEFT half (including mid) → hi = mid
"""


def optimal_approach1(arr: list[int]) -> int:
    """
    
    """
    n = len(arr)
    s = 0
    e = n-1
    minimum = float("inf")

    while (s<=e):
        m = s + (e-s)//2

        if arr[s] <= arr[m]:
            if arr[s] < minimum:
                minimum = arr[s]
                s = m
            else:
                s = m+1

        else:
            if arr[m] < minimum:
                minimum = arr[m]
                e = m
            else:
                e = m-1

    return minimum



def optimal_approach2(arr: list[int]) -> int:
    """
        Complexity Analysis:
            - Time -> O(log n)
            - Space -> O(1)
    """
    n = len(arr)
    s = 0
    e = n-1

    while (s<=e):
        m = s + (e-s)//2

        if arr[s] == arr[m] == arr[e]:
            return arr[m]
        
        if arr[m] > arr[e]:
            s = m + 1
        else:
            e = m


if __name__ == "__main__":
    arr = [3,4,5,1,2]
    # arr = [4,5,6,7,0,1,2,3]
    # arr = [1,2,3,4,5]
    # arr = [1]
    # print(optimal_approach1(arr))
    print(optimal_approach2(arr))

