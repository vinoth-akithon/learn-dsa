"""
"""


def naive_approach(arr: list[int], k: int) -> int:
    """
        - Using Nested loop approach
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    n = len(arr)
    lar_arr_size = 0

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == k:
                lar_arr_size = max(lar_arr_size, j-i+1)
            
    return lar_arr_size

def optimal_approach(arr: list[int], k: int) -> int:
    """
        - Using Prefix Sum and hash table
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """
    n = len(arr)
    lar_arr_size = 0
    pre_sum = 0
    hash_map = {}

    for i in range(n):
        pre_sum += arr[i]
        
        if pre_sum == k:
            lar_arr_size = max(lar_arr_size, i+1)

        elif (pre_sum - k) in hash_map:
            s: int = hash_map[pre_sum - k]
            lar_arr_size = max(lar_arr_size, i-s)   

        if (pre_sum - k) not in hash_map:
            hash_map[pre_sum] = i 
    
    return lar_arr_size


if __name__ == "__main__":
    arr = [9, -3, 3, -1, 6, -5]; k = 0
    # arr = [6, -2, 2, -8, 1, 7, 4, -10]; k = 0
    print(naive_approach(arr, k))
    print(optimal_approach(arr, k))