def all_distinct_pairs(arr: list[int], t: int) -> list[tuple[int, int]]:
    """
        - Problem Link: https://www.geeksforgeeks.org/problems/all-distinct-pairs-with-given-sum/1
        - Keep two pointers one at start of the array `l` and another at end of the array `r`.
        - Keep a resultant array for keeping all the possible two sums.
        - Summing up the two pointers value
            - If the summation is equal to target `t`, Insert the two sum into resultant array.
            - Else if the summation is greater than the target, move the right pointer one step backward.
            - Else move the left pointer `l` one step forward
        - Complexity
            - Time -> O(n)
            - Space -> O(1)
    """
    arr.sort()
    n = len(arr)
    l, r = 0, n-1
    result = []
    while (l < r):
        s = arr[l] + arr[r]
        if s < t:
            l += 1
        elif s > t:
            r -= 1
        else:
            result.append(sorted((arr[l], arr[r])))
            pre = arr[l]
            l += 1
            while ((l < r) and (arr[l] == pre)):
                l += 1

    print(result)
    return sorted(result, key=lambda e: e[0])

if __name__ == "__main__":
    # arr = [2,2,2]; t = 4
    arr = [1, 5, 7, -1, 5]; t = 6
    print(all_distinct_pairs(arr, t))
            