"""

"""

def brute_force(n: int, m: int) -> int:
    """
        Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """

    for i in range(1,m+1):
        x = i ** n
        if x == m:
            return i
        elif x > m:
            return -1


def optimal_approach(n: int, m: int) -> int:
    """
    """
    if m < 2:
        return m
    
    s = 1
    e = m // n

    while (s <= e):
        mid = s + (e - s)//2

        if (mid ** n) == m:
            return mid
        elif (mid ** n) < m:
            s = mid+1
        else:
            e = mid-1
    return -1


if __name__ == "__main__":
    # n = 4; m = 69
    # n = 3; m = 27
    n = 1; m = 2

    # print(brute_force(n, m))
    print(optimal_approach(n, m))
