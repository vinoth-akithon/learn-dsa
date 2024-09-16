from collections import defaultdict


def max_sum_subarray(arr: list, K: int):
    max_sum = float("-inf")
    arr_sum = 0
    window_start = 0
    for window_end in range(len(arr)):
        arr_sum += arr[window_end]

        if window_end >= K-1:
            if arr_sum > max_sum:
                max_sum = arr_sum
            arr_sum -= arr[window_start]
            window_start += 1

    return max_sum


def smallest_subarr_given_sum(arr: list, K: int):
    smallest_subarr_size = float("inf")
    window_sum = 0
    window_start = 0
    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= K:
            current_window_size = window_end + 1 - window_start
            if current_window_size < smallest_subarr_size:
                smallest_subarr_size = current_window_size
            window_sum -= arr[window_start]
            window_start += 1

    return smallest_subarr_size


def longest_substring_k_distict_char(arr: list, K: int):
    window_start = 0
    hash_table = defaultdict(int)
    largest_subsring = float("-inf")

    for window_end in range(len(arr)):
        right_char = arr[window_end]
        hash_table[right_char] += 1

        while len(hash_table) > K:
            left_char = arr[window_start]
            hash_table[left_char] -= 1
            if hash_table[left_char] == 0:
                hash_table.pop(left_char)
            window_start += 1

        current_window_size = window_end + 1 - window_start
        if current_window_size > largest_subsring:
            largest_subsring = current_window_size
    return largest_subsring


def no_repeat_string(arr):
    window_start = 0
    max_length = 0
    hash_table = {}

    for window_end in range(len(arr)):
        right_char = arr[window_end]
        if right_char not in hash_table:
            hash_table[right_char] = window_end
        else:
            if hash_table[right_char] >= window_start:
                window_start = hash_table[right_char] + 1
            hash_table[right_char] = window_end

        current_window_size = window_end + 1 - window_start
        if current_window_size > max_length:
            max_length = current_window_size

    return max_length


if __name__ == "__main__":
    # arr = [2, 1, 5, 1, 3, 2]
    # k = 3
    # print(max_sum_subarray(arr, k))

    arr = [3, 4, 1, 1, 6]
    k = 8
    # print(smallest_subarr_given_sum(arr, k))

    arr = "cbbebi"
    k = 3
    # print(longest_substring_k_distict_char(arr, k))

    arr = "abccde"
    print(no_repeat_string(arr))
