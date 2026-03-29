"""
Quick Sort Algo
"""


def partition(arr: list[int], s: int, e: int):
    pivot = arr[e]

    partition_index = s - 1
    for i in range(s, e+1):
        if arr[i] <= pivot:
            partition_index += 1
            arr[i], arr[partition_index] = arr[partition_index], arr[i]
    return partition_index


def quick_sort(arr: list[int], s: int, e: int) -> list[int]:
    n = e - s + 1
    if n <= 0:
        return arr
    
    partition_index = partition(arr, s, e)

    quick_sort(arr, s, partition_index-1)
    quick_sort(arr, partition_index+1, e)
    return arr

if __name__ == "__main__":
    # arr = [1,2,3]
    arr = [10, 7, 8, 9, 1, 5]
    # print(partition(arr))
    print(quick_sort(arr, 0, len(arr)-1))