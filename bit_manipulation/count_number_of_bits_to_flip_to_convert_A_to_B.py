"""

"""


def brute_force(m: int, n: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(1) as we are no of bit is constant (either 32 or 64)
            - Space -> O(1)
    """
    cnt = 0

    while m or n:
        cnt += (m & 1) ^ (n & 1) # getting the last bit from both input and check whether differ
        m = m >> 1
        n = n >> 1

    return cnt

def optimal_approach(m: int, n: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(1) as we are no of bit is constant (either 32 or 64)
            - Space -> O(1)
    """
    cnt = 0

    num = m ^ n # XOR gives differing bit as set bit

    for _ in range(32):
        cnt += num & 1
        num >>= 1

    return cnt


if __name__ == "__main__":
    m = 10; n = 7
    # m = 3; n = 4
    print(brute_force(m, n))
    print(optimal_approach(m, n))
