"""

"""


def naive_approach(arr: list[int]) -> list[int]:
    """
        - Using Auxiliary arrays
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """
    n = len(arr)
    pos_arr = []
    neg_arr = []

    for i in range(n):
        if arr[i] > 0:
            pos_arr.append(arr[i])
        else:
            neg_arr.append(arr[i])

    i = 0
    for pos, neg in zip(pos_arr, neg_arr):
        arr[i] = pos
        arr[i+1] = neg
        i += 2

    return arr


def optimal_approach(arr: list[int]) -> list[int]:
    """
        - Using Auxiliary arrays
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """
    n = len(arr)
    temp_arr = [0] * n
    pos = 0
    neg = 1

    for i in range(n):
        if arr[i] > 0:
            temp_arr[pos] = arr[i]
            pos += 2
        else:
            temp_arr[neg] = arr[i]
            neg += 2

    return temp_arr

if __name__ == "__main__":
    arr = [3,1,-2,-5,2,-4]
    # print(naive_approach(arr))
    print(optimal_approach(arr))