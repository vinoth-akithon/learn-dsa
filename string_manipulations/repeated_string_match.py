"""
#NOTE: Comeback and Solve Later
"""


def brute_force(a: str, b: str) -> int:
    """
        - Approach:
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """
    # Edge Case
    hash_set = set()
    for c in a:
        hash_set.add(c)

    cnt = 1
    while len(a) < len(b):
        a += a
        cnt += 1

    i = 0
    j = 0
    
    while j < len(b):
        if b[j] not in hash_set:
            return 0
        if b[j] != a[i]:
            # Reset j to 0
            j = 0
            i += 1
            if len(a)-i < len(b):
                a += a
                cnt += 1
        else:
            i += 1
            j += 1

    return cnt
            


if __name__ == "__main__":
    # a = "abcd"; b = "cdabcdab"
    # a = "a"; b = "aa"
    a = "abc"; b = "wxyz"
    print(brute_force(a, b))