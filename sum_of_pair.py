"""
Given a sorted array and a number x, find a pair in an array whose sum is closest to x.

Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
Output: 22 and 30

Input: arr[] = {1, 3, 4, 7, 10}, x = 15
Output: 4 and 10
"""


def sum_of_pair(arr, x):
    array_length = len(arr)
    minimum = float("inf")
    index_1 = index_2 = 0
    left_index, right_index = 0, array_length -1
    while left_index < right_index:
        differnce = abs(x - (arr[left_index] + arr[right_index]))
        if differnce < minimum:
            index_1 = left_index
            index_2 = right_index
            minimum = differnce

        if arr[left_index] + arr[right_index] > x:
            right_index -= 1
        else:
            left_index +=1
    return [arr[index_1], arr[index_2]]

input_array = [10, 22, 28, 29, 30, 40]; target = 54
# input_array = [1, 3, 4, 7, 10]; target = 15

print(sum_of_pair(input_array, target))