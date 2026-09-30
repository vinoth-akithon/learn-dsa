"""
Given a prefix sum array, we have to calculate the original array from which the prefix array formed.
"""


def original_arr(prefix_arr: list[int]) -> list[int]:
    """
    Complexity Analysis:
        - Time -> O(n)
        - Space -> O(n)

    :param arr: Description
    :type arr: list[int]
    :return: Description
    :rtype: list[int]
    """
    n = len(prefix_arr)
    arr = [prefix_arr[0]]

    for i in range(1, n):
        arr.append(prefix_arr[i] - prefix_arr[i - 1])
    
    return arr


if __name__ == "__main__":
    arr = [1, 3, 6, 10, 15]
    print(original_arr(arr))
