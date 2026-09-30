"""

"""


def brute_force(arr: list[str]) -> str:
    """
        - Checking against each elements and char
        - Complexity Analysis:
            - Time -> O(n * min(len(arr)))
            - Space -> O(P)
    """
    m = len(arr)
    if m == 0:
        return ""
    elif m == 1:
        return arr[0]

    long_pref = []
    n = len(arr[0])
    i = 0
    while i < n:
        char = arr[0][i]
        for j in range(1, m):
            if i >= len(arr[j]) or arr[j][i] != char:
                return "".join(long_pref)
        long_pref.append(char)
        i += 1

    return "".join(long_pref)


def optimal_approach(arr: list[str]) -> str:
    """
        - Applying sorting for easily identify the common prefix
        - Complexity Analysis:
            - Time -> O(n * log n + M)
            - Space -> O(P)
    """
    n = len(arr)
    if n == 0:
        return ""
    elif n == 1:
        return arr[0]

    arr.sort()

    first = arr[0]
    last = arr[n-1]
    res = []

    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return "".join(res)
        res.append(first[i])

    return "".join(res)





if __name__ == "__main__":
    arr = ["flower", "flow", "flight"]
    # arr = ["apple", "banana", "grape", "mango"]
    # arr = ["ab", "a"]
    print(brute_force(arr))
    print(optimal_approach(arr))
