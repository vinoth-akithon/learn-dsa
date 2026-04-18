"""

"""


def naive_approach(arr: list[list[int]]) -> list[int]:
    """
        - Using Auxiliary set for holding visited position.
        
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(n^2)

    """
    m = len(arr)
    n = len(arr[0])
    
    direction = "right"
    r = 0
    c = 0
    visited = set()
    result: list[int] = []

    while (0 <= r < m) and (0 <= c < n) and (r,c) not in visited:
        visited.add((r,c))
        result.append(arr[r][c])

        if direction == "right":
            if c+1 < n and (r,c+1) not in visited:
                c += 1
            else:
                r += 1
                direction = "down"

        elif direction == "down":
            if r+1 < m and (r+1,c) not in visited:
                r += 1
            else:
                c -= 1
                direction = "left"

        elif direction == "left":
            if c-1 >= 0 and (r,c-1) not in visited:
                c -= 1
            else:
                r -= 1
                direction = "up"
        
        elif direction == "up":
            if r-1 >= 0 and (r-1,c) not in visited:
                r -= 1
            else:
                c += 1
                direction = "right"

    return result


def optimal_approach(arr: list[list[int]]) -> list[int]:
    """
        - Using boundaries setup.

        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    m = len(arr)
    n = len(arr[0])
    res = []
    t = 0
    b = m-1
    l = 0
    r = n-1

    while (t <= b) and (l <= r):
        
        for i in range(l, r+1):
            res.append(arr[t][i])
        t += 1

        for i in range(t, b+1):
            res.append(arr[i][r])
        r -= 1

        if t <= b:
            for i in range(r, l-1, -1):
                res.append(arr[b][i])
            b -= 1

        if l <= r: 
            for i in range(b, t-1, -1):
                res.append(arr[i][l])
            l += 1

    return res




if __name__ == "__main__":
    # arr = [
    #     [1,2,3,4],
    #     [12,13,14,5],
    #     [11,16,15,6],
    #     [10,9,8,7]
    # ]
    arr = [
        [1,2,3,4],
        [10,11,12,5],
        [9,8,7,6]]
    # arr = [
    #     [1]
    # ]
    # arr = [
    #     [1,2],
    #     [4,3]
    # ]
    # arr = [
    #     [1,2,3],
    #     [8,9,4],
    #     [7,6,5]
    # ]
    # print(naive_approach(arr))
    print(optimal_approach(arr))