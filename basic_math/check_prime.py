"""
- Prime property says a number should be prime only if it must have only two distinct factors (1 and number itself)
    - 1 is not prime (as it has only one factor (1))
    - 4 is not prime (as it has 3 factors (1, 2, 4))
"""
import math


def optimal_approach(n: int) -> bool:
    """
        - Using the square root symmetry property for getting all divisors algo.
        - Complexity Analysis:
            - Time -> O(sqrt(n))
            - space -> O(1)
    """
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    n = 7
    n = 13
    print(optimal_approach(n))
