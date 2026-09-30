"""
"""
import math
from itertools import permutations


def naive_approach(arr: list[int]) -> list[int]:
    """
        - Get all possible permutations of the given array.
        - Sort them in ascending order.
        - Iterate the sorted permutations list and compare against input arr.
        - If any one matched except last one, return the next permutation.
        - Else return the first permutation.

        - Complexity Analysis:
            - Time -> O(n n!)
            - Space -> O(n n!)
    """
    n = math.factorial(len(arr))
    input_tuple = tuple(arr)

    all_permutations = list(set(permutations(arr)))
    all_permutations.sort()
    
    for i in range(n):
        if input_tuple == all_permutations[i]:
            if i == n-1:
                return all_permutations[0]
            return all_permutations[i+1]
        

def optimal_approach(arr: list[int]) -> list[int]:
    """
        - We can find the next permutation by applying the following 4 condition.
            - Traverse the input array in reverse order find the first element that is less than the next element -> arr[i] < arr[i+1].
                - Keep this element as breaking point -> b = arr[i]
            - If no breaking point found, sort the input array in ascending order and return.
            - Traverse the input array in reverse order find the first element that is greater than the breaking point. -> arr[j] > b.
                - Swap these elements b and arr[j]
            - Reverse the sub array arr[b+1:]

        - Complexity Analysis:
            - Time -> O(n log n)
            - Space -> O(1)
    """
    n = len(arr)

    # Condition 1
    b = -1
    for i in range(n-2, -1, -1):
        if arr[i] < arr[i+1]:
            b = i
            break

    # Condition 2
    if b == -1:
        arr.sort()
        return arr
    
    # Condition 3
    for j in range(n-1, -1, -1):
        if arr[j] > arr[b]:
            arr[b], arr[j] = arr[j], arr[b]
            break
    
    l = b + 1
    r = n-1
    while (l < r):
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr





if __name__ == "__main__":
    arr = [2,1,3]
    # arr = [3,1,2]
    # arr = [3,2,1]
    # arr = [1,2,3]
    # arr = [1,1,5]
    # print(naive_approach(arr))
    print(optimal_approach(arr))

