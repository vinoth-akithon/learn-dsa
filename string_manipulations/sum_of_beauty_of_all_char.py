"""

"""

from collections import Counter

def brute_force(s: str) -> int:
    """
        - Finding all possible sub string
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(n)
    """
    n = len(s)
    sum_ = 0
    sub_strs = []
    for i in range(n):
        for j in range(i+1, n):
            items = Counter(s[i:j+1]).items()
            items = sorted(items, key=lambda x: x[1])
            sum_ += items[-1][1] - items[0][1]

    return None


if __name__ == "__main__":
    # s = "xyx"
    s = s = "aabcbaa"
    print(brute_force(s))

