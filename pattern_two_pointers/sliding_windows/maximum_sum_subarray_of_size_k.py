def maximum_sum(arr: list[int], k: int) -> int:
    n = len(arr)
    if n < k:
        return 0
    
    max_sum = 0
    current_sum = 0
    
    # for e in range(k):
    #     current_sum += arr[e]
    # max_sum = max(max_sum, current_sum)

    # for e in range(k, n):
    #     current_sum = current_sum - arr[e-k] + arr[e]
    #     max_sum = max(max_sum, current_sum)

    for e in range(n):
        current_sum += arr[e]

        if e >= k:
            current_sum = current_sum - arr[e-k]

        if e >= k-1:
            max_sum = max(max_sum, current_sum)

    return max_sum


if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]; k=3
    # arr = [2, 3, 4, 1, 5]; k=2 
    print(maximum_sum(arr, k)) 