"""
Given an array of integers and a target.
We have find all the sub array count whose xor of all the the elements equals to k
"""

def brute_force_approach(arr: list[int], k) -> int:
    """
        - Using nested loop approach and find all the sub arrays and check xor of its elements equal to target.
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    n = len(arr)
    cnt = 0
    # res_arr = []
    for i in range(n):
        res = arr[i]
        if arr[i] == k:
            cnt += 1
        
        for j in range(i+1, n):
            res ^= arr[j]
            
            if res == k:
                cnt += 1
                # res_arr.append(arr[i:j+1])
    # print(res_arr)
    return cnt



def optimal_approach(arr: list[int], k) -> int:
    """
        - Using prefix xor approach.
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    n = len(arr)
    cnt = 0
    hash_map = {0: 1}
    pre = 0
    
    for i in range(n):
        pre ^= arr[i]
        
        if (pre ^ k) in hash_map:
            cnt += hash_map[pre ^ k]
        
        hash_map[pre] = hash_map.get(pre, 0) + 1
    return cnt



if __name__ == "__main__":
    # arr = [4, 2, 2, 6, 4]; k = 6 #[4, 2], [4, 2, 2, 6, 4], [2, 2, 6],[6]
    arr = [5, 6, 7, 8, 9]; k = 5
    print(brute_force_approach(arr, k))
    print(optimal_approach(arr, k))

