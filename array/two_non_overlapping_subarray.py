"""
"""


def brute_force(arr: list[int], t: int) -> int:
    """
    
    """
    sub_arrays = []

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sub_arr = arr[i:j+1]
            if sum(sub_arr) == t:
                sub_arrays.append([i, j, j-i+1])

    print(sub_arrays)
    non_overlapping_sub_arrays = []
    for i in range(1, len(sub_arrays)):
        if sub_arrays[i-1][1] < sub_arrays[i][0]:
            non_overlapping_sub_arrays.append(sub_arrays[i])

    s = 0
    e = 0
    window_sum = 0
    for e in range(len(arr)):
        window_sum += arr[e]

        while window_sum > t:
            window_sum -= arr[s]
            s += 1

        if s <= e and window_sum == t:
            sub_arrays.append(arr[s:e+1])
            s = e
            window_sum = arr[s]


    if len(sub_arrays) < 2:
        return -1
    
    sub_arrays.sort(key=lambda x: len(x))
    return len(sub_arrays[0]) + len(sub_arrays[1])


if __name__ == "__main__":
    # arr = [3,2,2,4,3]; t = 3
    # arr = [7,3,4,7]; t = 7
    # arr = [4,3,2,6,2,3,4]; t = 6
    # arr = [1,6,1]; t = 7
    # arr = [2,1,3,3,2,3,1]; t = 6 
    # arr = [3, 1, 1, 1, 2, 3]; t = 3
    arr = [1,1,1,1]; t = 2
    print(brute_force(arr, t))
