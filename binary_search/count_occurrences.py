"""

"""

def first_occurrence(arr: list[int], t: int) -> int:
    """
        - Using binary search

        - Complexity Analysis:
            - Time -> O(log n)
            - Space -> O(1)
    """
    n = len(arr)
    s = 0
    e = n-1
    ans = n

    while (s <= e):
        m = s + (e-s)//2

        if arr[m] >= t:
            e = m -1
            if arr[m] == t:
                ans = m
        else:
            s = m + 1
        
    return ans

def last_occurrence(arr: list[int], t: int) -> int:
    """
        - Using binary search

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

        if arr[m] <= t:
            s = m + 1
            if arr[m] == t:
                ans = m
        else:
            e = m -1
        
    return ans




def count_occurrence(arr: list[int], t: int) -> int:
    """
    
    """
    first_occur = first_occurrence(arr, t)
    last_occur = last_occurrence(arr, t)
    if first_occur > last_occur:
        return 0
    return last_occur - first_occur + 1


if __name__ == "__main__":
    # arr = [2, 2 , 3 , 3 , 3 , 3 , 4]; t = 3
    arr = [1, 1, 2, 2, 2, 2, 2, 3]; t=100
    print(count_occurrence(arr, t))