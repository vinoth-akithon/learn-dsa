"""
Given an array of intergers, return the resultant array whose elements are the product of all the other elements except element itself.
"""


def naive_approach(arr: list[int]) -> list[int]:
    """
    - Using nested for loop
    - Complexity Analysis:
        - Time -> O(n^2)
        - Space -> O(n)

    :param arr: Description
    :type arr: list[int]
    :return: Description
    :rtype: list[int]
    """

    n = len(arr)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= arr[j]
        result.append(product)
    return result


def better_approach(arr: list[int]) -> list[int]:
    """
    Using Prefix sum approach
    - Complexity Analysis:
        - Time -> O(n)
        - Space -> O(n)

    :param arr: Description
    :type arr: list[int]
    :return: Description
    :rtype: list[int]
    """

    n = len(arr)
    prefix_sum = [1]
    for i in range(n - 1):
        prefix_sum.append(prefix_sum[i] * arr[i])

    suffix_sum = [1] * n
    for i in range(n - 1, 0, -1):
        suffix_sum[i - 1] = suffix_sum[i] * arr[i]
    # print(suffix_sum)

    result = []
    for i in range(n):
        result.append(prefix_sum[i] * suffix_sum[i])

    return result


def optimal_approach(arr: list[int]) -> list[int]:
    """
    - Calculate the product of the entire array and then iterate and find the each product by dividing the current element.
    - But it only works when all the elements are positive.
    - If only one zero present in the array, the zero presented position only has the product value, everything else whould be zero.
    - If more than zero present in the input array, all the elements in the resultant array would be zero.

    - Complexity Analysis:
        - Time -> O(n)
        - Space -> O(n)

    :param arr: Description
    :type arr: list[int]
    :return: Description
    :rtype: list[int]
    """

    n = len(arr)
    zeros = 0
    zero_index = 0
    product = 1

    for i in range(n):
        if arr[i] == 0:
            zeros += 1
            zero_index = i
        else:
            product *= arr[i]

    result = [0] * n
    if zeros == 0:
        for i in range(n):
            result[i] = int(product / arr[i])
    elif zeros == 1:
        result[zero_index] = product
    return result


def using_power_function(arr: list[int]) -> int:
    """
    - Same as optimal approach (using division operator), but here using power function.
    - Complexity Analysis:
        - Time -> O(n)
        - Space -> O(n)
    
    :param arr: Description
    :type arr: list[int]
    :return: Description
    :rtype: int
    """
    n = len(arr)
    zeros = 0
    zero_index = 0
    product = 1

    for i in range(n):
        if arr[i] == 0:
            zeros += 1
            zero_index = i
        else:
            product *= arr[i]

    result = [0] * n
    if zeros == 0:
        for i in range(n):
            result[i] = int(product * pow(arr[i], -1))
    elif zeros == 1:
        result[zero_index] = product
    return result

def using_log_operator(arr: list[int]) -> int:
    pass



if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]  # result = [120, 60, 40, 30, 24]
    # arr = [1, 2, 0, 3, 4] # result = [0, 0, 24, 0, 0]
    # arr = [1, 2, 0, 0, 3]  # result = [0,0,0,0,0]
    print(naive_approach(arr))
    print(better_approach(arr))
    print(optimal_approach(arr))    
    print(using_power_function(arr))
