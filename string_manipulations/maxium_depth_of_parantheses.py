"""

"""


def brute_force(s: str) -> int:
    """
        - Keep increasing the level variable when we encounter open parenthesis and and keep decreasing
        the level when we encounter close parentheses
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    
    """
    max_level = 0
    level = 0

    for c in s:
        if c == "(":
            level += 1
            max_level = max(max_level, level)
        elif c == ")":
            level -= 1

    return max_level


if __name__ == "__main__":
    # s = "(1+(2*3)+((8)/4))+1"
    s = "(1)+((2))+(((3)))"
    print(brute_force(s))