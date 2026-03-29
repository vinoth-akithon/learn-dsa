"""

"""


def selection_sort(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n-1):
        lar_idx = 0
        for j in range(n-i):
            if arr[j] > arr[lar_idx]:
                lar_idx = j
        arr[n-1-i], arr[lar_idx] = arr[lar_idx], arr[n-1-i]
    return arr

def selection_sort2(arr: list[int]) -> list[int]:
    n = len(arr)
    for i in range(n-1, 0, -1):
        lar_idx = 0
        for j in range(i+1):
            if arr[j] > arr[lar_idx]:
                lar_idx = j
        arr[i], arr[lar_idx] = arr[lar_idx], arr[i]
    return arr

def recursive_approach(arr: list[int], n: int, l: int=0, c: int=0) -> list[int]:
    # Base Condition
    if n <= 0:
        return arr
    
    if c > n:
        arr[l], arr[n] = arr[n], arr[l]
        return recursive_approach(arr, n-1, 0, 0)
    else:
        if arr[c] > arr[l]:
            l = c
        return recursive_approach(arr, n, l, c+1)
    
if __name__ == "__main__":
    arr = [10, 2]
    print(selection_sort(arr))
    print(selection_sort2(arr))
    print(recursive_approach(arr, len(arr)-1))

