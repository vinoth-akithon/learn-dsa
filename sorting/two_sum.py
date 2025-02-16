import sys
sys.path.append(".")

from sorting.merge_sort import merge_sort


def two_sum(arr: list[int], target: int) -> tuple[int, int] | None:
    arr = merge_sort(arr)
    n = len(arr)
    i = 0
    while i < n:
        j = i + 1
        while j < n:
            if (arr[i] + arr[j]) == target:
                return arr[i], arr[j]
            elif (arr[i] + arr[j]) > target:
                break
            else:
                j += 1
        i += 1
    return None

if __name__ == "__main__":
    arr = [2,7,3,5,9]; target= 12
    # arr = [0, -1, 2, -3, 1]; target = -2
    # arr = [1, -2, 1, 0, 5]; target = 0
    print(two_sum(arr, target))