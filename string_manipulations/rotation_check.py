"""
Given two string, check one string is a rotation of another string.
"""

def rotate(s: str) -> str:
     return s[1:] + s[0]

def brute_force(s: str, t: str) -> bool:
    """
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(n)
    """
    m = len(s)
    n = len(t)

    if m != n:
         return False

    i = 0
    while i < m:
        if s == t:
            return True
        s = rotate(s)
        i += 1

    return False


def optimal_approach(s: str, t: str) -> bool:
    """
        - Doubling the given string and check against the target present in the new string
        - Complexity Analysis:
            - Time -> O(2n)
            - Space -> O(n)
    """
    m = len(s)
    n = len(t)

    if m != n:
        return False

    s += s
    if t in s:
        return True

    return False


if __name__ == "__main__":
    s = "rotation"; goal = "tionrota"
    # s = "hello"; goal = "lohelx"
    # print(brute_force(s, goal))
    print(optimal_approach(s, goal))