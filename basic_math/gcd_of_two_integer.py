"""

"""



def brute_force(x: int, y: int) -> int:
    """
        Complexity Analysis:
            - Time -> O(m) -> minimum value
            - Space -> O(1)
    """
    se = x if x < y else y
    gcd = 1
    for i in range(2, se+1):
        if (x % i == 0) and (y % i == 0):
            gcd = i
    return gcd


def better_approach(x: int, y: int) -> int:
    """
        Complexity Analysis:
            - Time -> O(min(x, y))
            - Space -> O(1)
    """
    se = x if x < y else y
    for i in range(se, 1, -1):
        if (x % i == 0) and (y % i == 0):
            return i
    return 1


def optimal_approach(x: int, y: int) -> int:
    """
    Euclidean algorithm for finding GCD of two numbers.

    GCD of x and y  when x > y
        - Repeatedly subtract the smaller number from the larger number until the one of them become zero.
        - if one become zero, other being the GCD of x and y.  
    """
    while (0 not in [x, y]):
        if x > y:
            x = x - y
        else:
            y = y - x
    return x if x else y

if __name__ == "__main__":
    x = 1; y = 9
    print(brute_force(x, y))
    print(better_approach(x, y))
    print(optimal_approach(x, y))