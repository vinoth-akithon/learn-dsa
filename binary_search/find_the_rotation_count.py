"""
Given an right rotated array, we have to find the rotation count.

Right rotation means: moving some elements from end to start of the sequence and moving remaining elements one step to right
"""


def brute_force(arr: list[int]) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)

    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return i+1
        
    return 0



def optimal_approach(arr: list[int]) -> int:
    """
        - Complexity Analysis:
            - Time -> O(log n)
            - Space -> O(1)
    """
    n = len(arr)
    s = 0
    e = n-1

    while (s < e):
        m = s + (e-s)//2

        if arr[m] > arr[e]:
            s = m+1
        else:
            e = m

    return s



if __name__ == "__main__":
    arr = [15, 18, 2, 3, 6, 12]
    # arr = [7, 9, 11, 12, 5]
    # arr = [7, 9, 11, 12, 15]
    print(brute_force(arr))
    print(optimal_approach(arr))