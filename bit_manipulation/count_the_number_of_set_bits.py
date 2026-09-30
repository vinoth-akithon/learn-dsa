"""
"""


def brute_force(n: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(log n)
            - Space -> O(log n)
    """
    binary = bin(n)[2:]
    cnt = 0
    for c in binary:
        if c == "1":
            cnt += 1

    return cnt

def better_approach(n: int) -> int:
    """
            - Complexity Analysis:
                - Time -> O(log n)
                - Space -> O(1)
    """
    cnt = 0
    while n > 0:
        cnt += n & 1
        n >>= 1

    return cnt

def optimal_approach(n: int) -> int:
    """
            - Complexity Analysis:
                - Time -> O(k) -> no of set bit (faster than checking all bits)
                - Space -> O(1)
    """
    cnt = 0

    while n:
        n = n & (n-1)
        cnt += 1

    return cnt

if __name__ == "__main__":
    n = 5
    print(brute_force(n))
    print(better_approach(n))
    print(optimal_approach(n))