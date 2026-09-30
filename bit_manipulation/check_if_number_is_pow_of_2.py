"""
"""


def optimal_approach(n: int) -> bool:
    """
        - Complexity Analysis
            - Time -> O(1)
            - Space -> O(1)
    """
    return n > 0 and n & (n-1) == 0


if __name__ == "__main__":
    n = 1
    print(optimal_approach(n))