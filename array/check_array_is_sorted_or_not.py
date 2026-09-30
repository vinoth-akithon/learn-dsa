"""
Checking whether the array is sorted or not
"""


def optimal_approach(arr: list[int]) -> bool:
    """
        - solve using Sorted array property where each element is should be less than or equal to the next element.
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    if n < 2:
        return True
    
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return False
    return True


if __name__ == "__main__":
    # arr = [1,4,3]
    arr = [1,2,3]
    print(optimal_approach(arr))