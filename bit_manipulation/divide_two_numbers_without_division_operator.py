"""

Two's complement is a way/operation used to represent the number of an integer.

Identity -> -n = ~n + 1 (two's complement of n)
"""

INT_MIN = -2**31
INT_MAX = 2**31 -1

def get_quotient(n: int, d: int, cnt: int, sign: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(dividend)
            - Space -> O(dividend)
    """
    # Base condition
    if n - d < 0:
        return -cnt if sign < 0 else cnt
    
    n -= d
    cnt += 1
    return get_quotient(n, d, cnt, sign)


def brute_force(n: int, d: int) -> int:
    """
            - Note: Maximum recursion depth exceed problem occur for large dividend and small divisor
            - Complexity Analysis:
                - Time -> O(dividend)
                - Space -> O(dividend)
    """
    if n == INT_MIN and d == -1:
        return INT_MAX
    elif d == 1:
        return n
    
    sign = 1
    if n < 0 and d < 0:
        sign = 1
    elif n < 0 or d < 0:
        sign = -1

    return get_quotient(abs(n), abs(d), 0, sign)


def optimal_approach1(n: int, d: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(log n)
            - Space -> O(1)
    """
    if n == INT_MIN and d == -1:
        return INT_MAX
    elif d == 1:
        return n
    
    sign = 1
    if n < 0 and d < 0:
        sign = 1
    elif n < 0 or d < 0:
        sign = -1

    n = abs(n)
    d = abs(d)
    q = 0

    while n >= d:
        curr = d
        mul = 1

        while n >= curr + curr:
            curr += curr
            mul += mul

        n -= curr
        q += mul

    if q > INT_MAX and sign == 1:
        return INT_MAX
    if q > INT_MAX and sign == -1:
        return INT_MIN

    return -q if sign == -1 else q


def optimal_approach2(n: int, d: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(log n/d * log n/d)
            - Space -> O(1)
    """
    if n == INT_MIN and d == -1:
        return INT_MAX
    elif d == 1:
        return n
    
    sign = 1
    if n < 0 and d < 0:
        sign = 1
    elif n < 0 or d < 0:
        sign = -1

    n = abs(n)
    d = abs(d)
    q = 0

    while n >= d:
        po = 0

        while n >= (d << po+1):
            po += 1

        n -= d << po
        q += 1 << po

    if q > INT_MAX and sign == 1:
        return INT_MAX
    if q > INT_MAX and sign == -1:
        return INT_MIN  

    return -q if sign == -1 else q




if __name__ == "__main__":
    # n = 10; q = 2
    n = 22; q = 7

    # n = 2_147_483_647; q= 1
    # print(brute_force(2_147_483_647, 1000))
    print(optimal_approach1(n, q))
    print(optimal_approach2(n, q))
