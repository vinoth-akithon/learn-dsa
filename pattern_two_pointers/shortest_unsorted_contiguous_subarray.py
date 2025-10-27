def shortest_unsorted_contiguous_subarray(arr: list[int]) -> int:
    """
        - Brute force approch using efficent sorting algo.
        - Complexity Analysis:
            - Time -> O(n logn)
            - Space -> O(n) for storing the sorted version for comparition
    """
    sorted_arr = sorted(arr)
    n = len(arr)
    l, r = 0, n-1

    while l <= r and arr[l] == sorted_arr[l]:
        l += 1
    while r >= l and arr[r] == sorted_arr[r]:
        r -= 1
    return r - l + 1

def shortest_unsorted_contiguous_subarray2(arr: list[int]) -> int:
    """
        - Optimized approch using sliding window
        - Complexity Analysis:
            Time -> O(n)
            Space -> O(n)
    """
    n = len(arr)
    l, r = 0, n-1

    while (l < n-1 and arr[l] <= arr[l + 1]):
        l += 1

    if l == r:
        return 0

    while (r > 0 and arr[r] >= arr[r-1]):
        r -= 1

    window = arr[l: r+1]
    window_min = min(window)
    window_max = max(window)

    for i in range(l-1, -1, -1):
        if arr[i] > window_min:
            l -= 1

    for i in range(r+1, n):
        if arr[i] < window_max :
            r += 1

    return r - l + 1

def shortest_unsorted_contiguous_subarray3(arr: list[int]) -> int:
    """
        - Optimized approch using two pointers.
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(arr)
    l, r = -1, -2
    max_seen, min_seen = arr[0], arr[n-1]
    
    for i in range(1, n):
        if arr[i] == max_seen:
            continue
        elif arr[i] >= max_seen:
            max_seen = arr[i]
        else:
            r = i
    
    for i in range(n-2, -1, -1):
        if arr[i] == min_seen:
            continue
        elif arr[i] < min_seen:
            min_seen = arr[i]
        else:
            l = i
    return r - l + 1


if __name__ == "__main__":
    arr = [2,6,4,8,10,9,15]
    # arr = [1,2,3,4]
    # arr = [1]
    # arr = []
    # print(shortest_unsorted_contiguous_subarray(arr))
    # print(shortest_unsorted_contiguous_subarray2(arr))
    # print(shortest_unsorted_contiguous_subarray3(arr))