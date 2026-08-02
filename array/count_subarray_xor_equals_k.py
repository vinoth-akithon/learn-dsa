"""
"""


def brute_force_approach(arr: list[int], k: int) -> int:
    """
        - Using nested loop approach for finding all the sub array whose XOR matches k.

        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(n) 
    """
    n = len(arr)
    cnt = 0

    for i in range(n):
        pre = 0
        for j in range(i, n):
            pre ^= arr[j]
        
            if pre == k:
                cnt += 1

    return cnt


def optimal_approach(arr: list[int], k: int) -> int:
    """
        - Using Prefix sum hash map frequency approach.

        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n) -. Due to auxiliary hash map
    """
    n = len(arr)
    cnt = 0
    hash_map = {0: 1}
    ps = 0

    for i in range(n):
        # Adding curr element to the ps
        ps ^= arr[i]

        # Checking the previous ps exist in the hash map
        cnt += hash_map.get(ps^k, 0)
        
        # Increase the count of the ps in the hashmap if already exist else insert new one
        hash_map[ps] = hash_map.get(ps, 0) + 1

    return cnt



if __name__ == "__main__":
    # arr = [4, 2, 2, 6, 4]; k = 6
    arr = [5, 6, 7, 8, 9]; k = 5
    print(brute_force_approach(arr, k))
    print(optimal_approach(arr, k))
