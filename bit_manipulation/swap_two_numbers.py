"""

"""

def optimal_approach(a: int, b: int) -> tuple[int, int]:
    """
        - Complexity Analysis:
            - Time -> O(1)
            - Space -> O(1)
    """
    a ^= b
    b ^= a
    a ^= b
    return a, b


if __name__ == "__main__":
    a = 5; b = 10
    print(optimal_approach(a, b))
    