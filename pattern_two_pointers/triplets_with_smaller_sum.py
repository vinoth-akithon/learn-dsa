def triplets_with_smaller_sum(arr: list[int], t: int) -> int:
    count = 0
    n = len(arr)
    arr.sort()
    for i in range(0, n-2):
        l, r = i+1, n-1
        while (l < r):
            s = arr[i] + arr[l] + arr[r]
            if s < t:
                count += r-l
                l += 1
            else:
                r -= 1
    return count

if __name__ == "__main__":
    arr = [-2, 0, 1, 3]; target = 2
    # arr = [5, 1, 3, 4, 7]; target = 12
    print(triplets_with_smaller_sum(arr, target))