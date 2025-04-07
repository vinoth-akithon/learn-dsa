"""
    - Opposite direction two pointers approch.
    - LCode: https://leetcode.com/problems/3sum/description/
"""


import sys
sys.path.append(".")
from three_sum import three_sum


def four_sum(arr: list[int], t: int=0) -> list[tuple[int, int, int, int]]:
    """
        - Sort the input array using efficient sorting algo (like merge sort)
        - Iterate the array until n-3 times
        - Keep track of possible resultant four sum into a array.
        - Fix the one element(iterative pointer) and calculate the possible unique triplets for the remaining subarray.
            - Call the three sum function for the specified range and get all the possible triplets.
            - Construct the possible four sums by combining the possible triplets.
            - Keep moving the iterative pointer one step backward until we get the non repeative element.
        - Return the resultant possible four sums.
        - Complexity:
            - Time -> O(n log(n)) + O(n^3) ~= O(n^3)
            - Space -> O(1)
    """
    arr.sort()
    n = len(arr)
    result = []
    i = 0
    while (i < n-3):
        three_sum_target = t - arr[i]
        possible_three_sums = three_sum(arr[i+1:], three_sum_target)
        for x in possible_three_sums:
            result.append((arr[i], *x))
        pre = arr[i]
        i += 1
        while (i < n-3) and (arr[i] == pre):
            i += 1
    return result 



if __name__ == "__main__":
    # arr = [1,2,3,4,5,6,7,9]; t = 8
    arr = [0,0,0,0, 0]; t = 0
    # arr = [-1,0,1,2,-1,-4]; t = 0
    print(four_sum(arr, t))
