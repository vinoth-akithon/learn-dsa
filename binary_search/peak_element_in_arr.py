"""
A element in the array called peak only if it's greater than the previous element and next element.
"""

def brute_force(arr: list[int]) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)

    for i in range(n):
        l = (i == 0) or arr[i] > arr[i-1]
        r = (i == n-1) or arr[i] > arr[i+1]
        
        if l and r:
            return i
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

    while (s <= e):
        m = s + (e-s)//2

        if (m == 0 or arr[m-1] < arr[m]) and (m == n-1 or arr[m] > arr[m+1]):
            return m
        
        if (m == 0 or arr[m-1] < arr[m]) and (m == n-1 or arr[m] < arr[m+1]):
            s = m+1
        else:
            e = m


if __name__ == "__main__":
    # arr = [1,2,3,4,5,6,7,8,5,1]
    # arr = [1,2,1,3,5,6,4]
    # arr = [1]
    # arr = [1,2]
    arr = [2,1]
    print(brute_force(arr))
    print(optimal_approach(arr))