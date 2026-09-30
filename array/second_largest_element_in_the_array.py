"""
Second Largest Element in the Array
"""


def naive_approach(arr: list[int]) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n logn) -> due to sorting
            - Space -> O(1)
    """
    n = len(arr)
    if n < 2:
        return -1

    arr.sort()
    return arr[n-2]

def better_approach(arr: list[int]) -> int:
    """
        - Complexity Analysis:
            - Time -> O(2n) ~= O(n) 
            - Space -> O(1)
    """
    n = len(arr)
    if n < 2:
        return -1

    fl = arr[0]
    for i in range(1, n):
        if arr[i] > fl:
            fl = arr[i]
    
    sl = float("-inf")
    for i in range(n):
        if arr[i] > sl and arr[i] < fl:
            sl = arr[i]
    return sl

def optimal_approach(arr: list[int]) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    if n < 2:
        return -1

    fl = arr[0]
    sl = float("-inf")

    for i in range(1, n):
        if arr[i] > fl:
            sl = fl
            fl = arr[i]
        elif arr[i] > sl and arr[i] < fl:
            sl = arr[i]

    return sl        



if __name__ == "__main__":
    arr = [3,7,5,6,2]
    print(naive_approach(arr))
    print(better_approach(arr))
    print(optimal_approach(arr))

