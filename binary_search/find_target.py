"""
- Given an sorted array of integers and a target, we need to find whether the given target exist in the array.
- If find return that index else return -1
- All the items in the given are unique

"""

def brute_force(arr: list, t: int) -> int:
    """
        - Using linear search (checking all the possibilities)

        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)

    for i in range(n):
        if arr[i] == t:
            return i
        
    return -1


def optimal_approach_iterative(arr: list, t: int) -> int:
    """
        - Using Binary search

        - Complexity Analysis:
            - Time -> O(log n)
            - Space -> O(1)
    """
    n = len(arr)
    s = 0
    e = n-1
    
    while (s <= e):
        m = s + (e-s)//2

        if arr[m] == t:
            return m
        elif arr[m] > t:
            e = m-1
        else:
            s = m+1

    return -1

def optimal_approach_recursive(arr: list, t: int, s: int, e: int) -> int:
    """
        - Using Binary search

        - Complexity Analysis:
            - Time -> O(log n)
            - Space -> O(log n) -> Due to recursive stack
    """
    # Base condition
    if s > e:
        return -1
    
    m = s + (e-s)//2
    
    if arr[m] == t:
        return m
    elif arr[m] > t:
        return optimal_approach_recursive(arr,t, s, m-1)
    else:
        return optimal_approach_recursive(arr,t, m+1, e)

    

if __name__ == "__main__":
    arr = [1,2, 3]; t = 3
    # print(brute_force(arr, t))
    print(optimal_approach_iterative(arr, t))
    print(optimal_approach_recursive(arr, t, 0, len(arr)-1))

