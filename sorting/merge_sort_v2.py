"""
Merge Sort Algo
"""

def merging_algo(arr1: list[int], arr2: list[int]) -> list[int]:
    l = r = 0
    ln = len(arr1)
    rn = len(arr2)
    merged_arr = []

    while (l < ln and r < rn):
        if arr1[l] < arr2[r]:
            merged_arr.append(arr1[l])
            l += 1
        else:
            merged_arr.append(arr2[r])
            r += 1

    while (l < ln):
        merged_arr.append(arr1[l])
        l +=1

    while (r < rn):
        merged_arr.append(arr2[r])
        r +=1
    
    return merged_arr


def merge_sort(arr: list[int]) -> list[int]:
    # Base condition
    n = len(arr)
    if len(arr) <= 1:
        return arr

    mid = n // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    left_sorted_arr = merge_sort(left_arr)
    right_sorted_arr = merge_sort(right_arr)

    # Merging
    return merging_algo(left_sorted_arr, right_sorted_arr)
    


if __name__ == "__main__":
    arr = [10, 2, 8]
    print(merge_sort(arr))