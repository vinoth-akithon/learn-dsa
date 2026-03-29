"""

"""


def shell_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    gap = n//2
    
    while (gap > 0):
        for i in range(gap, n, gap):
            picked = arr[i]
            j = i - gap

            while (j >= 0 and picked < arr[j]):
                arr[j+gap] = arr[j]
                j -= gap

            arr[j+gap] = picked

        gap //= 2
    return arr

if __name__ == '__main__':
    # arr = [22, 34, 25, 12, 64, 11, 90, 88, 45]
    arr = [11, 2]
    print(shell_sort(arr))