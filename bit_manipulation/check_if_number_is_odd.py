"""

"""


def brute_force(n: int) -> bool:
    """
        - Complexity Analysis
            - Time -> O(1)
            - Space -> O(1)
    """
    if n % 2 != 0:
        return True
    return False


def optimal_approach(n: int) -> bool:
    """
        - Complexity Analysis
            - Time -> O(1)
            - Space -> O(1)
    """
    return n & 1 != 0


if __name__ == "__main__":
    n = 2
    print(brute_force(n))
    print(optimal_approach(n))
