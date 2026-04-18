"""

Given a array and k, we need to count all the number of sub array sum matches k.
"""


def naive_approach(arr: list[int], k: int) -> int:
    """
        - Find all possible sub arrays using nested loop and check the current sub array sum equals to k.
        
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    n = len(arr)
    cnt = 0

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]

            if curr_sum == k:
                cnt += 1
        
    return cnt


def optimal_approach(arr: list[int], k: int) -> int:
    """
        - Using Prefix Sum and Set approach.
        
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """
    n = len(arr)
    hash_map = {0: 1}
    cnt = 0
    pre_sum = 0

    for i in range(n):
        pre_sum += arr[i]

        pre_pre_sum = (pre_sum - k)
        if pre_pre_sum in hash_map:
            cnt += hash_map[pre_pre_sum]

        hash_map[pre_sum] = hash_map.get(pre_sum, 0) + 1
    return cnt



if __name__ == "__main__":
    # arr = [3, 1, 2, 4]; k = 6
    # arr = [1,2,3]; k = 3
    # arr = [1,-1,0]; k = 0
    arr = [0, 0, 0]; k = 0
    # arr = [3, -3, 1, 1, 1]; k = 3
    # arr = [1, -1, 1, -1, 1]; k = 0
    print(naive_approach(arr, k))
    print(optimal_approach(arr, k))
    print(subarraySum(arr, k))
