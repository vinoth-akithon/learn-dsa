"""
- XOR of a sequence follows a predictable pattern

0 ^ 1 -> 0001 -> 1
1 ^ 2 -> 0011 -> 3
3 ^ 3 -> 0000 -> 0
0 ^ 4 -> 0100 -> 4

4 ^ 5 -> 0001 -> 1
1 ^ 6 -> 0111 -> 7
7 ^ 7 -> 0000 -> 0
0 ^ 8 -> 1000 -> 8
"""


def brute_force(L: int, R: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(R-L)
            - Space -> O(1)
    """
    ans = 0
    for i in range(L, R+1):
        ans ^= i

    return ans


def get_xor_from_1_N(N: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(1)
            - Space -> O(1)
    """
    n = N % 4
    if n == 0:
        return N
    elif n == 1:
        return 1
    elif n == 2:
        return N+1
    elif n == 3:
        return 0


def optimal_approach(L: int, R: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(1)
            - Space -> O(1)
    """
    return get_xor_from_1_N(R) ^ get_xor_from_1_N(L-1)

if __name__ == "__main__":
    # L = 3; R = 5
    # L = 1; R = 3
    L = 18920; R = 40866
    print(brute_force(L, R))
    print(optimal_approach(L, R))
