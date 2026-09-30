"""
Docstring for split_array_into_two_subarray
"""


def optimal_approach(arr: list[int]) -> list[int] | None:
    n = len(arr)
    total = sum(arr)
    prefix_sum = arr[0]
    # total = prefix_sum[0:pivot-1] + arr[pivot] +  suffix_sum[pivot+1:n]

    for i in range(1, n):
        suffix_sum = total - prefix_sum
        if suffix_sum == prefix_sum:
            return [arr[:i], arr[i:]]
        prefix_sum += arr[i]
    return None 


if __name__ == "__main__":
    # arr = [1 , 2 , 3 , 4 , 5 , 5 ]
    # arr = [ 4, 1, 2, 3 ]
    arr = [ 4, 3, 2, 1]

    print(optimal_approach(arr))