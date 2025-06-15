
def two_sum_less_than_k(arr: list[int], K: int) -> list[int]:
    """
        - GFG Link -> https://www.geeksforgeeks.org/problems/pair-with-largest-sum-which-is-less-than-k-in-the-array/1
        - Method -> Opposite Direction Two Pointers
        - Keep a variable to hold the resultant maximum pair sum which is less than the K.
        - Intialize left and right pointers.
        - Loop through until the left pointer reaches the right pointer.
            - Calculate the sum and compare with K.
            - If the current sum is greater than or Equal to the K move the right pointer one step backward.
            - Else move the left pointer one step forward and check current sum againt the resultant maximum pair, if it greater than the previous one update the resultant pair sum with current pair sum.
        - Retuns the resultant maximun pair sum.
        - Complexity Analysis:
            Time -> O(n logn) -> Due to sorting
            Space -> O(1) or O(n) -> Depends upon sorting algo we used
    """
    arr.sort()
    n = len(arr)
    l, r = 0, n - 1
    maximum_pair_sum = float("-inf")
    maximum_pair = [-1, -1]
    
    while (l < r):
        s = arr[l] + arr[r]
        if s < K:
            if s > maximum_pair_sum:
                maximum_pair_sum = s
                maximum_pair = [arr[l], arr[r]]
            l += 1
        else:
            r -= 1
    return maximum_pair



if __name__ == "__main__":
    arr = [2, 3, 4, 6, 8, 10]; k = 10
    # arr = [2, 3, 4, 6, 8, 10]; k = 0
    print(two_sum_less_than_k(arr, k))