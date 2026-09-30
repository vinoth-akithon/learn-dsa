"""
Remove Duplicates form the sorted array
"""


def naive_approach(arr: list[int]) -> list[int]:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(d) -> no. of non duplicate elements
    """
    n = len(arr)
    if n < 2:
        return arr
    
    hash_map = {}
    for i in range(n):
        e = arr[i]
        if e not in hash_map:
            hash_map[e] = 1
    
    for i, k in enumerate(hash_map.keys()):
        arr[i] = k

    return arr[:i+1]


def optimal_approach(arr: list[int]) -> list[int]:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    if n < 2:
        return arr
    
    s = 0
    for e in range(1, n):
        if arr[e] != arr[s]:
            s += 1
            arr[s] = arr[e]

    return arr[:s+1]
            


if __name__ == "__main__":
    arr = [1,2,2,3,4,4]
    print(naive_approach(arr))
    print(optimal_approach(arr))
