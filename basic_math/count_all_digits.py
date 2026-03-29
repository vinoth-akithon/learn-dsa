"""
Count all digit of a number

"""

import math

def naive_approach(n: int) -> int:
    """
    - Complexity Analysis:
        - Time -> O(log10(N))
            - Here we are dividing the input repeatedly in the factor of 10.
        - Space -> O(1)
    """
    if n == 0:
        return 1
    count = 0
    while (n > 0):
        n //= 10
        count += 1
    return count


def optimal_approach(n: int) -> int:
    """
    - log10 gives the number of digits for a positive number. we need to add to 1 for balancing the fractional part and for converting integer.
        - log10(9999) -> 3.9542425094393248
        - log10(1999) -> 3.300812794118117
    - Complexity Analysis:
        - Time -> O(1)
            - Here we are dividing the input repeatedly in the factor of 10.
        - Space -> O(1)
    """
    if n is 0:
        return 1
    return int(math.log10(n) + 1)


if __name__ == "__main__":
    # n = 12345
    n = 0
    print(naive_approach(n))
    print(optimal_approach(n))
