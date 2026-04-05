"""

"""


def naive_approach(arr: list[int], t: int) -> tuple[int, int]:
    """
        - Using Linear search and Nested loop
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    n = len(arr)

    for i in range(n-1):
        nt = t - arr[i]
        for j in range(i+1, n):
            if arr[j] == nt:
                return (i, j)

    return (-1, -1)


def better_approach(arr: list[int], t: int) -> tuple[int, int]:
    """
        - Using Two Pointers
        - Complexity Analysis:
            - Time -> O(n log n)
            - Space -> O(n)
    """
    n = len(arr)
    s = 0
    e = n-1
    nums_with_index = [(arr[i], i) for i in range(n)]
    
    nums_with_index.sort(key=lambda e:e[0])

    while (s < e):
        if (nums_with_index[s][0] + nums_with_index[e][0]) < t:
            s += 1
        elif (nums_with_index[s][0] + nums_with_index[e][0]) > t:
            e -= 1
        else:
            return (nums_with_index[s][1], nums_with_index[e][1])

    return (-1, -1)


def optimal_approach(arr: list[int], t: int) -> tuple[int, int]:
    """
        - Using Hash Map
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """
    n = len(arr)
    hash_map = {}

    for i in range(n):
        if arr[i] in hash_map:
            return (hash_map[arr[i]], i)
        else:
            j = t - arr[i]
            hash_map[j] = i

    return (-1, -1)


if __name__ == "__main__":
    arr = [2,6,5,8,11]; t = 14
    # arr = [2,6,5,8,11]; t = 15

    # print(naive_approach(arr, t))
    print(better_approach(arr, t))
    # print(optimal_approach(arr, t))