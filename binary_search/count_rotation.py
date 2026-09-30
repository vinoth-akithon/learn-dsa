"""
Find out how many times array has rotated
"""


def brute_force(arr: list[int]) -> int:
    """
    - Complexity Analysis:
        - Time -> O(n)
        - Space -> O(1)
    """
    n = len(arr)
    min_val = arr[0]
    min_idx = 0

    for i in range(1,n):
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i

    return min_idx

def better_approach(arr: list[int]) -> int:
    """
        Complexity Analysis:
            - Time -> O(k) number times it's right rotated
            - Space -> O(1)
    """
    n = len(arr)
    
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            return i


def optimal_approach(arr: list[int]) -> int:
    """
    Complexity Analysis:
        - Time -> O(log n)
        - Space -> O(1)
    """
    n = len(arr)
    s = 0
    e = n-1

    while (s <= e):
        m = s + (e-s)//2

        if arr[s] == arr[m] == arr[e]:
            return m
        
        if arr[m] > arr[e]:
            s = m+1
        else:
            e = m




if __name__ == "__main__":
    arr = [3,4,5,1,2]
    # print(brute_force(arr))
    print(better_approach(arr))
    # print(optimal_approach(arr))