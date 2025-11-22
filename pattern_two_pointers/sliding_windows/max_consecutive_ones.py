def max_consecutive_ones(arr: list[int]):
    n = len(arr)
    max_ones = 0
    current_max_ones = 0
    s = 0

    for e in range(n):
        if arr[e] == 0:
            current_max_ones = e - s
            max_ones = max(current_max_ones, max_ones)
            s = e+1
            
    current_max_ones = n - s
    max_ones = max(current_max_ones, max_ones)

    return max_ones
    