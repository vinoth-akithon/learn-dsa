"""
Also called Dutch national flag problem and sort colors
"""


def naive_approach(arr: list[int]) -> list[int]:
    """
        - Using Hash map as auxiliary data structure.
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    hash_map = {0: 0, 1: 0, 2: 0}
    
    for i in range(n):
        hash_map[arr[i]] += 1

    i = 0
    for k, v in hash_map.items():
        for _ in range(v):
            arr[i] = k
            i += 1
    
    return arr

def optimal_approach(arr: list[int]) -> list[int]:
    """
        - Using Two pointers approach
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    s = 0
    e = n-1


    i = 0
    while (i <= e):
        if arr[i] == 0:
            arr[s], arr[i] = arr[i], arr[s]
            s += 1
            i += 1
        elif arr[i] == 2:
            arr[e], arr[i] = arr[i], arr[e]
            e -= 1
        else:
            i += 1

    return arr

if __name__ == "__main__":
    # arr = [1, 0, 2, 1, 0]
    # arr = [0,0,1,0,2]
    arr = [2,0,2,1,1,0]
    # print(naive_approach(arr))
    print(optimal_approach(arr))