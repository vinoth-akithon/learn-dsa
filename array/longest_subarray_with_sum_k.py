"""
Longest Sub-array with Sum k (Only positive)
"""


def naive_approach(arr: list[int], k: int) -> int:
    """
        - Using nested loop approach
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


def better_approach(arr: list[int], k: int) -> int:
    """
        - Using Sliding windows approach (But only applicable for Positive elements)
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    s = 0
    lar_arr_size = 0
    curr_sum = 0

    for e in range(n):
        curr_sum += arr[e]

        while (s <= e) and (curr_sum > k):
            curr_sum -= arr[s]
            s += 1
        
        if curr_sum == k:
            lar_arr_size = max(lar_arr_size, e-s+1)
    
    return lar_arr_size


def optimal_approach(arr: list[int], k: int) -> int:
    """
        - Using Prefix Sum and hash table
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    lar_arr_size = 0
    pre_sum = 0
    hash_map = {}

    for i in range(n):
        pre_sum += arr[i]
        
        if pre_sum == k:
            lar_arr_size = max(lar_arr_size, i+1)

        if (pre_sum - k) in hash_map:
            s = hash_map.get(pre_sum - k)
            lar_arr_size = max(lar_arr_size, i-s)   

        if (pre_sum - k) not in hash_map:
            hash_map[pre_sum] = i 
    
    return lar_arr_size





if __name__ == "__main__":
    # arr = [10, 5, 2, 7, 1, 9]; k = 15 
    # arr = [-3, 2, 1]; k = 6
    # arr = [9, -3, 3, -1, 6, -5]; k = 0
    # arr = [1, 2, 3, -3, 3]; k = 3
    arr =  [1, 2, 1, 1, 1]; k = 3
    # print(naive_approach(arr, k))
    # print(better_approach(arr, k))
    print(optimal_approach(arr, k))