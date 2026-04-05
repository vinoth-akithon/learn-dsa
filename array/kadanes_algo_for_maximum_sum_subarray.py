"""
Variation of Maximum subarray sum. Here we instead of returning maximum sum,
we return sub array itself.
"""

def optimal_approach(arr: list[int]) -> list[int]:
    """
    """
    n = len(arr)
    s = e = temp_s = 0
    max_sum = float("-inf")
    curr_sum = 0

    for i in range(n):
        curr_sum += arr[i]
        if arr[i] > curr_sum:
            temp_s = i
            curr_sum = arr[i]

        if curr_sum > max_sum:
            max_sum = curr_sum
            s = temp_s
            e = i

    return arr[s:e+1]
        



if __name__ == "__main__":
    # arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    arr = [-2, -3, -7, -2, -10, -4]  
    print(optimal_approach(arr))
