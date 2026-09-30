"""
To find the length of longest subarray whose sum equals to k.
"""


def naive_approach(arr: list[int], k: int) -> int:
    """
    - Using nested loop.
    - Complexity Analysis:
        - Time -> O(n ^ 2)
        - Space -> O(1)
    
    :param arr: Description
    :type arr: list[int]
    :return: Description
    :rtype: int
    """

    n = len(arr)
    max_length = 0

    for i in range(n):
        sum = arr[i]
        for j in range(i+1, n):
            sum += arr[j]
            if sum == k:
                max_length = max(j-i+1, max_length)
    return max_length


def optimal_approach(arr: list[int], k: int) -> int:
    """
    - Using Prefix sum approach.
    - Complexity Analysis:
        - Time -> O(n)
        - Space -> O(1)

    :param arr: Description
    :type arr: list[int]
    :param k: Description
    :type k: int
    :return: Description
    :rtype: int
    """

    n = len(arr)
    prefix_sum = [arr[0]]
    max_length = 0

    for i in range(1, n):
        sum = prefix_sum[i-1] + arr[i]
        prefix_sum.append(sum)
        if sum == k:
            max_length = max(max_length, i+1)
    return max_length

if __name__ == "__main__":
    arr = [10, 5, 2, 7, 1, -10]; k = 15 
    # arr = [-5, 8, -14, 2, 4, 12]; k = -5
    # arr = [10, -10, 20, 30]; k = 5
    print(naive_approach(arr, k))
    print(optimal_approach(arr, k))


    # prefix_sum = [10, 15, 17, 24, 25, 15]
    # prefix_sum = [-5, 3, -11, -9, -5, 7]

    # arr = [5, 2, -3, 4, 7]; k= 3
    # prefix_sum = [5, 7, 4, 8, 15]; k=3



    # a + b = k
    # b = k - a

    # 10 - 15 = -5 -> prefix_sum = 10 -> longest = 0 -> {10: 0} 
    # 15 - 15 = 0 -> prefix_sum = 15 -> longest = j-i+1 = 1-0+ 1 = 2 -> {10: 0, 5: 1}
    # 15 - 2 = 13 -> prefix_sum = 17 -> longest = 2 -> {10: 0, 5: 1, 2: 2}
    # 15 - 7 = 8 -> prefix_sum = 24 -> longest = 2 -> {10: 0, 5: 1, 2:2, 7: 3}
    # 15 - 1 = 14 -> 

    # prefix_sum = 10 | 10 - 15 | longest = 0 | {10: 0}
    # prefix_sum = 15 | 15 - 15 | longest = 2 | {10: 0, 15: 1}
    # prefix_sum = 17 | 17 - 15 | longest = 2 | {10: 0, 15: 1, 17: 2}
    # prefix_sum = 24 | 24 - 15 | longest = 2 | {10: 0, 15: 1, 17: 2, 24: 3}
    # prefix_sum = 25 | 25 - 15 | longest = 4 | {10: 0, 15: 1, 17: 2, 24: 3}
    # prefix_sum = 15 |  