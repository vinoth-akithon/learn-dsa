"""
    Given an array, find the average of all contiguous 
    subarrays of size `K` in it.

    Input: 
        Array = [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5
    Output:
        [2.2, 2.8, 2.4, 3.6, 2.8]

    Brute force solution:
        Time Complexity: O(N * K) 

    Time Complexity: O(N)
    Space Comlexity: O(1)
"""

import timeit


def average_of_subarray1(input_arr: list[int], K: int) -> list[float]:
    result = []
    for i in range(len(input_arr)-K+1):
        sub_array_sum = 0
        for j in range(i, i+K):
            sub_array_sum += input_arr[j]
        result.append(sub_array_sum/K)
    return result


def average_of_subarray2(input_arr: list[int], K: int) -> list[float]:
    result = []
    for i in range(len(input_arr)-K+1):
        result.append(sum(input_arr[i:i+K])/K)
    return result


def average_of_subarray3(input_arr: list[int], K: int) -> list[float]:
    return [sum(input_arr[i:i+K])/K for i in range(len(input_arr)-K+1)]


def average_of_subarray4(input_arr: list[int], K: int) -> list[float]:
    result = []
    window_start = 0
    window_sum = 0

    for i in range(len(input_arr)):
        window_sum += input_arr[i]
        # sliding the window only if the window size exeeds
        if i >= K-1:
            result.append(window_sum/K)
            window_sum -= input_arr[window_start]
            window_start += 1
    return result


input_arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
K = 5

if __name__ == "__main__":
    print(average_of_subarray1(input_arr, K))
    print(average_of_subarray2(input_arr, K))
    print(average_of_subarray3(input_arr, K))
    print(average_of_subarray4(input_arr, K))
    # time_taken = timeit.timeit("average_of_subarray1(input_arr, K)",
    #                            setup="from __main__ import average_of_subarray1,input_arr,K")
    # print(f"time_taken_by_average_of_subarray1: {time_taken}")
    # time_taken = timeit.timeit("average_of_subarray2(input_arr, K)",
    #                            setup="from __main__ import average_of_subarray2,input_arr,K")
    # print(f"time_taken_by_average_of_subarray2: {time_taken}")
    # time_taken = timeit.timeit("average_of_subarray3(input_arr, K)",
    #                            setup="from __main__ import average_of_subarray3,input_arr,K")
    # print(f"time_taken_by_average_of_subarray3: {time_taken}")
    # time_taken = timeit.timeit("average_of_subarray4(input_arr, K)",
    #                            setup="from __main__ import average_of_subarray4,input_arr,K")
    # print(f"time_taken_by_average_of_subarray4: {time_taken}")
