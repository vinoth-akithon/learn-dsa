"""
Linear Search
"""

def linear_search(arr: list[int], t: int) -> int:
    """
        - Checking whether the given element present in the given array, by iterating all the elements.
        - If current iter pointer points to the target value, return the iter pointer (as it's index of the element)
        - If target not present in the element, then we can return -1.
    """

    n = len(arr)
    for i in range(n):
        if arr[i] == t:
            return i
    return -1

if __name__ == "__main__":
    arr = [1,2,5,20,3,50]
    print(linear_search(arr, 20))
    print(linear_search(arr, 2))
