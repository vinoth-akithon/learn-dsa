"""
"""


def brute_force(n: int) -> int:
    """
        Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """

    ans = 0

    for i in range(1, n+1):
        square = i ** 2
        if square > n:
            break
        else:
            ans = i

    return ans


def optimal_approach(n: int) -> int:
    """
        Complexity Analysis:
            - Time -> O(log n)
            - Space -> O(1)
    """
    ans = 0
    s = 1
    e = n//2

    while (s<=e):
        m = s + (e-s)//2

        if (m ** 2) <= n:
            ans = m
            s = m+1
        else:
            e = m-1
    return ans

if __name__ == "__main__":
    n = 9
    # print(brute_force(n))
    print(optimal_approach(n))