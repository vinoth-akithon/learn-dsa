def container_with_most_water(arr: list[int]):
    max_area = float("-inf")
    n = len(arr)
    l = 0
    r = n - 1
    while (l < r):
        h = min(arr[l], arr[r])
        w = r - l
        a = h * w
        if (a > max_area):
            max_area = a
        if arr[l] < arr[r]:
            l += 1
        else:
            r -= 1
    return max_area

if __name__ == "__main__":
    arr = [1,8,6,2,5,4,8,3,7]
    print(container_with_most_water(arr))