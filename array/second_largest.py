"""
Second largest element
"""

def second_largest(arr: list[int]) -> int:
    fl = sl = -1

    for i in range(len(arr)):
        if arr[i] > fl:
            sl = fl
            fl = arr[i]
        elif arr[i] != fl and arr[i] > sl:
            sl = arr[i]

    return sl



if __name__  == "__main__":
    arr = [3,2,5]
    # arr = [1, 2, 4, 7, 7, 5]
    print(second_largest(arr))