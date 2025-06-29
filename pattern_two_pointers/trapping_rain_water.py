def trapping_rain_water(arr: list[int]) -> int:
    """
        - Brute forch approch
        - For each element find the max_left and max_right walls, then pick the min wall(which affecting the area)
        - Calculate the water contains using min height of the wall and current height.
        - water = min(maxleft, maxright) - current wall height
        - If the current wall height is max than the computed one, then where no water trap happen.
    """
    n = len(arr)
    water = 0
    for i in range(0, n):
        if i == 0:
            left_max = 0
        else:
            left_max = max(arr[:i])
        if i == n-1:
            right_max = arr[n-1]
        else:
            right_max = max(arr[i+1:])

        current_water = min(left_max, right_max) - arr[i]
        if current_water > 0:
            water += current_water
    return water


def trapping_rain_water2(arr: list[int]) -> int:
    """
        - Using pre-computed left and right max values
        - For each element find the max_left and max_right walls, then pick the min wall(which affecting the area)
        - Calculate the water contains using min height of the wall and current height.
        - water = min(maxleft, maxright) - current wall height
        - If the current wall height is max than the computed one, then where no water trap happen.
        - Complexity Analysis
            - Time -> O(n)
            - Space -> O(n)
    """
    n = len(arr)
    water = 0
    if n == 0:
        return water
    
    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = arr[0]
    for i in range(1, n):
        left_max[i] = max(arr[i], left_max[i-1])

    right_max[-1] = arr[-1]
    for i in range(n-2, -1, -1):
        right_max[i] = max(arr[i], right_max[i+1])

    for i in range(n):
        # As the previous minimum height is always greater than equal to the current wall
        water = min(left_max[i], right_max[i]) - arr[i]
    return water

def trapping_rain_water3(arr: list[int]) -> int:
    n = len(arr)
    if not n:
        return 0
    left_max, right_max, water = 0, 0, 0
    l, r = 0, n-1
    
    while (l < r):
        if arr[l] <= arr[r]:
            if arr[l] >= left_max:
                left_max = arr[l]
            else:
                water += left_max - arr[l]
            l += 1
        else:
            if arr[r] >= right_max:
                right_max = arr[r]
            else:
                water += right_max - arr[r]
            r -= 1
    return water

if __name__ == "__main__":
    # arr = [0,1,0,2,1,0,1,3,2,1,2,1]
    arr = [4,2,0,3,2,5]
    # arr = []
    # print(trapping_rain_water(arr))
    # print(trapping_rain_water2(arr))
    print(trapping_rain_water3(arr))

