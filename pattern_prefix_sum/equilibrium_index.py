"""
Return if equilibrium idex is exist else return -1.

Equilibrium index of an array is the index whose lower indices value sum equal to the higher indices.

If multiple indcies exist return the first equilibrium index from left.
"""

def naive_approcah(arr: list[int]) -> int:
    pass


def equilibrium_index(arr: list[int]) -> int:
    """
    Complexity Analysis:
        - Time -> O(3n) ~= O(n)
        - Space -> O(2n) ~= O(n)
    
    :param arr: Description
    :type arr: list[int]
    :return: Description
    :rtype: int
    """
    n = len(arr)

    prefix_sum = [arr[0]]
    for i in range(1, n):
        prefix_sum.append(prefix_sum[i-1] + arr[i])

    suffix_sum = [0] * n
    suffix_sum[-1] = arr[-1]
    for i in range(n-2, -1 ,-1):
        suffix_sum[i] = suffix_sum[i+1] + arr[i] 
    
    print(prefix_sum)
    print(suffix_sum)
    for i in range(n):
        if prefix_sum[i] is suffix_sum[i]:
            return i
    return -1


def optimal_approch(arr: list[int]) -> int:
    # prefix_sum[0:pivot-1] + arr[pivot] + suffix_sum[pivot+1:n-1] = total_sum
    n = len(arr)
    prefix_sum = 0
    total = sum(arr)

    for pivot in range(n):
        suffix_sum = total - prefix_sum - arr[pivot]
        if prefix_sum == suffix_sum:
            return pivot
        prefix_sum += arr[pivot]
    return -1



if __name__ == "__main__":
    arr =  [1, 2, 0, 3]
    arr = [1, 1, 1, 1]
    # arr = [-7, 1, 5, 2, -4, 3, 0]
    # print(equilibrium_index(arr))
    print(optimal_approch(arr))