"""
    Check whether the given array is having duplicate element in it or not.
    Link: https://leetcode.com/problems/contains-duplicate/description/
"""
import sys
sys.path.append(".")
from sorting.merge_sort import merge_sort

def contains_duplicate1(arr: list[int]) -> bool:
    """
        - Brute Force Approch (using Two loop)
        - Time -> O(n^2)
        - Space -> O(1)
    """
    n = len(arr)
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                return True
    return False


def contains_duplicate2(arr: list[int]) -> bool:
    """
        - Better Approch (Using sorting)
        - Time -> O(n * log(n))
        - Space -> O(1)
    """
    n = len(arr)
    merge_sort(arr)
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            return True
    return False



def contains_duplicate3(arr: list[int]) -> bool:
    """
        - Optimal (Using Hash Set)
        - Time -> O(n)
        - Space -> O(n)
    """
    n = len(arr)
    hash_set = set()
    for i in range(n):
        if arr[i] in hash_set:
            return True
        hash_set.add(arr[i])
    return False


if __name__ == "__main__":
    arr = [2,5,6,7,2,5,4]
    # arr = [2,3,4]
    print(contains_duplicate3(arr))