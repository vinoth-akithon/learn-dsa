"""

"""

def bubble_sort(arr: list[int]) -> list[int]:
    """
    Complexity Analysis:
        - Time -> O(n^2)
        - Space -> O(1)
    
    """
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def bubble_sort2(arr: list[int]) -> list[int]:
    """
    Complexity Analysis:
        - Time -> O(n^2)
        - Space -> O(1)
    
    """
    n = len(arr)
    for i in range(n-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def recursive_way(arr: list[int], c: int, n: int, is_swapped=False) -> list[int]:
    """
    Complexity Analysis:
        - Time -> O(n^2)
        - Space -> O(n) -> due to recursion stack
    
    """
    # Base condition:
    if n == 0:
        return arr
    
    if c == n:
        # Optimization tech
        if not is_swapped:
            return arr
        return recursive_way(arr, 0, n-1)
    else:
        if arr[c] > arr[c+1]:
            is_swapped = True
            arr[c], arr[c+1] = arr[c+1], arr[c]
        return recursive_way(arr, c+1, n, is_swapped) 


if __name__ == "__main__":
    # arr = [10, 2, 8]
    arr = [2,8,10]
    # print(bubble_sort(arr))
    # print(bubble_sort2(arr))
    print(recursive_way(arr, 0, len(arr)-1))