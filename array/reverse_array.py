"""
    Reverse the order of the given array
    Link: https://www.geeksforgeeks.org/problems/reverse-an-array/0
"""

def reverse_array1(arr: list[int]) -> None:
    """
        - Brute Force Approch (Using Temporary Array)
        - Time -> O(n)
        - Space -> O(n)
    """
    n = len(arr)
    temp = []
    for i in range(n-1, -1, -1):
        temp.append(arr[i])
    for j in range(n):
        arr[j] = temp[j]


def reverse_array2(arr: list[int]) -> None:
    """
        - Using Recursion
        - Time -> O(n)
        - Space -> O(n)
    """
    tmp = []
    reverse_array2_helper(arr, 0, tmp)
    n = len(tmp)
    for j in range(n):
        arr[j] = tmp[j]

def reverse_array2_helper(arr: list[int], i: int, tmp: list[int]) -> None:
    # Base condition
    n = len(arr)
    if i >= n:
        return
    reverse_array2_helper(arr, i+1, tmp)
    tmp.append(arr[i])


def reverse_array3(arr: list[int]) -> None:
    """
        - Optimal Approch (Using Two Pointers)
        - Time -> O(n)
        - Space -> O(1)
    """
    n = len(arr)
    i = 0; j = n-1
    while (i < j):
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


if __name__ == "__main__":
    arr = []
    reverse_array3(arr)
    print(arr)