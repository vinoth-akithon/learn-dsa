

def first_missing_integer(arr: list[int]) -> int:
    arr.sort()
    n = len(arr)
    if arr[0] != 0:
        return 0
    for i in range(n-1):
        if arr[i+1] != arr[i] + 1:
            return arr[i] + 1
    return arr[n-1] + 1


if __name__ == "__main__":
    # arr = [3,0,1]
    # arr = [0,1]
    arr = [9,6,4,2,3,5,7,0,1]
    # arr = [0]
    # arr = [1]
    print(first_missing_integer(arr))