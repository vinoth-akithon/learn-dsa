"""
    - Opposite direction two pointers approch
    - LCode: https://leetcode.com/problems/3sum/description/
"""


import sys
sys.path.append(".")
from two_sum_sorted import two_sum_sorted2

def three_sum(arr: list[int], t: int=0) -> list[tuple[int, int, int]]:
    """
        - Sort the input array using efficient sorting algo (like merge sort)
        - Iterate the array until n-2 times
        - keep track of possible resultant triplet array.
        - Calculate the expected two sum using the target and current iterative pointer.
            - Call the two sum function for the specified range and get the possible two sums array.
            - update the current iterative pointer with the collected two sums and insert into the resultant array.
        - Return the resultant possible triplets.
        - Complexity:
            - Time -> O(n log(n)) + O(n^2) ~= O(n^2)
            - Space -> O(1)
    """
    arr.sort()
    n = len(arr)
    result = []
    i = 0
    while (i < n-2):
        two_sum_target = t - arr[i]
        possible_two_sums = two_sum_sorted2(arr[i+1:], two_sum_target)
        for x in possible_two_sums:
            result.append((arr[i], *x))
        pre = arr[i]
        i += 1
        while ((i < n-2) and (arr[i] == pre)):
            i += 1
    return result



if __name__ == "__main__":
    # arr = [1,2,3,4,5,6,7,9]; t = 8
    # arr = [0,0,0, 0]; t = 0
    arr = [-1,0,1,2,-1,-4]; t = 0
    print(three_sum(arr, t))
