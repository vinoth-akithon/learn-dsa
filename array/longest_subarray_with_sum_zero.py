"""
Given array contains both positive and negative elements
"""

def brute_force_approach(arr: list[int]) -> int:
    """
        - Using nested loop approach to find all the sub arrays that matches 0.
        
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    n = len(arr)
    lar = 0
    
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += arr[j]
            if s == 0:
                lar = max(lar, j-i+1)
    return lar



def optimal_approach(arr: list[int]) -> int:
    """
        - Using Prefix sum and hash map approach (As the input array can contain negatives so sliding windows is not possible).
        
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """
    n = len(arr)
    lar = 0
    hash_map = {}
    pre = 0

    for i in range(n):
        pre += arr[i]

        if pre == 0:
            lar = max(lar, i+1)

        if pre in hash_map:
            lar = max(lar, i-hash_map[pre])

        if pre not in hash_map:
            hash_map[pre] = i

    return lar

if __name__ == "__main__":
    arr = [9, -3, 3, -1, 6, -5]
    # arr = [6, -2, 2, -8, 1, 7, 4, -10]
    print(brute_force_approach(arr))
    print(optimal_approach(arr))