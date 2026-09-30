"""


"""


def brute_force(s: str) -> str:
    """
        - Skip the open parentheses when we encounter at level 1 and skip the closed parentheses when we encounter level 0
        - Complexity Analysis:
            - Time -> O(n + n)
            - Space -> O(n) -> for storing output string
    """

    res = ""
    level = 0

    for c in s:
        if c == "(":
            level += 1
            if level > 1:
                res += c
        else:
            level -= 1
            if level > 0:
                res += c

    return res


if __name__ == "__main__":
    s = "((()))"
    print(brute_force(s))
