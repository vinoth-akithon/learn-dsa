"""

"""


def brute_force(s: str) -> bool:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(n)
    """
    stack = []
    hash_map = {")": "(","]": "[", "}": "{"}
    open_ = hash_map.values()

    for c in s:
        if c in open_:
            stack.append(c)
        else:
            if len(stack) == 0:
                return False
            elif stack[-1] == hash_map[c]:
                stack.pop()

    return len(stack) == 0


if __name__ == "__main__":
    # s = r"()[{}()]"
    # s = r"[()"
    s = r"]"

    print(s)
    print(brute_force(s))