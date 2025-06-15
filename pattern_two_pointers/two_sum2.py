def two_sum_sorted(arr: list[int], t: int) -> tuple[int, int]:
    """
        - LC Link -> https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
        - Keep two pointers one at start of the array `l` and another at end of the array `r`.
        - Summing up the two pointers value
            - If the summation is equal to target `t` return those pointers.
            - Else if the summation is greater than the target, move the right pointer one step backward.
            - Else move the left pointer `l` one step forward. 
        - Complexity
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    l = 0
    r = n-1
    while (l < r):
        s = arr[l] + arr[r]
        if s < t:
            l += 1
        elif s > t:
            r -= 1
        else:
            return l, r
    return -1,-1

def two_sum_sorted2(arr: list[int], t: int) -> list[tuple[int, int]]:
    """
        - Keep two pointers one at start of the array `l` and another at end of the array `r`.
        - Keep a resultant array for keeping all the possible two sums.
        - Summing up the two pointers value
            - If the summation is equal to target `t` return pointers. Insert the two sum into resultant array.
            - Else if the summation is greater than the target, move the right pointer one step backward.
            - Else move the left pointer `l` one step forward
        - Complexity
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    l = 0
    r = n-1
    result = []
    while (l < r):
        s = arr[l] + arr[r]
        if s < t:
            l += 1
        elif s > t:
            r -= 1
        else:
            result.append((arr[l], arr[r]))
            pre = arr[l]
            l += 1
            while ((l < n-1) and (arr[l] == pre)):
                l += 1
    return result
            


if __name__ == "__main__":
    arr = [2,2,2]; t = 4
    print(two_sum_sorted2(arr, t))