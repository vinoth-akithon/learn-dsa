"""
"""


def optimal_approach(n: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(1)
            - Space -> O(1)
    """
    return n | (n+1)


if __name__ == "__main__":
    n = 7
    print(optimal_approach(n))