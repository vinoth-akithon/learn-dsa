"""
    Minimum size subarray whose sum greater than or equal to the target.
"""

def mimimum_size_subarray(arr: list[int], t: int):
    n = len(arr)
    min_window_size = float("inf")
    current_window_sum = 0
    s = 0

    for e in range(n):
        current_window_sum += arr[e]

        while current_window_sum >= t:
            current_window_size = e - s + 1
            min_window_size = min(min_window_size, current_window_size)
            current_window_sum -= arr[s]
            s += 1

    return min_window_size if min_window_size != float("inf") else 0   

if __name__ == "__main__":
    # t = 7; arr = [2,3,1,2,4,3]
    # t = 4; arr = [1,4,4]
    t = 11; arr = [1,1,1,1,1,1,1,1]
    print(mimimum_size_subarray(arr, t))