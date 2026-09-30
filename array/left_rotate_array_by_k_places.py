"""
Left rotate the array by k places
"""

def arr_reverse(arr: list[int], s: int, e: int) -> None:
    while (s < e):
        arr[s], arr[e] = arr[e], arr[s]
        s += 1
        e -= 1

def optimal_approach(arr: list[int], k: int) -> list[int]:
    """
    """
    n = len(arr)
    k %= n
    arr_reverse(arr, 0, n-1)
    arr_reverse(arr, 0, n-1-k)
    arr_reverse(arr, n-1-k+1, n-1)
    return arr




if __name__ == "__main__":
    arr = [1,2,3,4,5]
    print(optimal_approach(arr, 7))


#     1,2,3,4,5 -> 5,4,3,2,1 -> 3,4,5,1,2

# 4 - 2 -> 2
# 5 - 2 -> 3