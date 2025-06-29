def dutch_national_flag(arr: list[int]) -> list[int]:
    n = len(arr)
    l, r, i = 0, n-1, 0

    while (i <= r):
        if arr[i] == 0:
            arr[l], arr[i] = arr[i], arr[l]
            l += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[r], arr[i] = arr[i], arr[r]
            r -= 1
    return arr


if __name__ == "__main__":
    arr = [1,0,2,1,0]
    # arr = [2,2,0,1,2,0]
    print(dutch_national_flag(arr))