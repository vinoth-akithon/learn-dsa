"""
Left rotate array by 1
"""


def optimal_approach(arr: list[int]) -> list[int]:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    if n < 2:
        return arr
    
    le = arr[0]
    for i in range(1, n):
        arr[i-1] = arr[i]
    
    arr[n-1] = le
    
    return arr





if __name__ == "__main__":
    arr = [1,2,3]
    print(optimal_approach(arr))