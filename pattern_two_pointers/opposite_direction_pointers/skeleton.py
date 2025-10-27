def opposite_direction_two_pointers(arr, t):
    n = len(arr)
    l, r = 0, n-1
    
    while (l < r):
        s = arr[l] + arr[r]
        if s == t:
            # Do something
            l += 1
            r -= 1
        elif s < t:
            l += 1
        else:
            r -= 1