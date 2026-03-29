"""

"""


def insertion_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(1, n):
        picked = arr[i]
        j = i-1
        while (j >= 0 and picked < arr[j]):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = picked
    return arr


def recursive_way(arr: list[int], n: int, i: int) -> list[int]:
    # Base condition
    if i >= n:
        return arr
    
    picked = arr[i]
    j = i-1
    while (j >= 0 and picked < arr[j]):
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = picked

    return recursive_way(arr, n, i+1)


if __name__ == '__main__':
    arr = [10]
    # print(insertion_sort(arr))
    print(recursive_way(arr, len(arr), 1))