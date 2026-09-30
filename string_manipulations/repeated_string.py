"""

"""


def brute_force(s: str, n: int) -> int:
    """
        - Approach: Forming the actual string of the given length
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """
    if s == "a":
        return n
    
    while len(s) < n:
        s += s[:n-len(s)]

    cnt = 0
    for c in s:
        if c == "a":
            cnt += 1

    return cnt


def better_approach(s: str, n: int) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    if s == "a":
        return n
    
    m = len(s)
    cnt = 0
    i = 0
    while i < n:
        if s[i%m] == "a":
            cnt += 1
        i += 1

    return cnt


def optimal_approach(s: str, n: int) -> int:
    """
        - Approach: Compute the number of occurrence of `a` in the given string and compute the occurrence of `a`
        in the remaining string.
        - Complexity Analysis:
            - Time -> O(m)
            - Space -> O(1)
    """
    if s  == "a":
        return n

    m = len(s)
    cnt = 0
    for c in s:
        if c == "a":
            cnt += 1
    
    q = n//m
    cnt *= q

    r = n%m
    for i in range(r):
        if s[i] == "a":
            cnt += 1

    return cnt

if __name__ == "__main__":
    s = "abcac"; n = 10
    # s = "a"; n = 1000000000000
    # s = "kmretasscityylpdhuwjirnqimlkcgxubxmsxpypgzxtenweirknjtasxtvxemtwxuarabssvqdnktqadhyktagjxoanknhgilnm"; n = 736778906400
    print(brute_force(s, n))
    print(optimal_approach(s, n))
