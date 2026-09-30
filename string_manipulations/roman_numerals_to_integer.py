"""

"""

def brute_force(s: str) -> int:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    sum_ = 0
    pre = 0
    for c in s:
        if mapping[c] > pre:
            sum_ += mapping[c] - 2 * pre
        else:
            sum_ += mapping[c]
        pre = mapping[c]

    return sum_


def better_approach(s: str) -> str:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    n = len(s)
    sum_ = 0
    for i in range(n-1):
        if mapping[s[i]] < mapping[s[i+1]]:
            sum_ -= mapping[s[i]]
        else:
            sum_ += mapping[s[i]]

    sum_ += mapping[s[n-1]]
    return sum_



if __name__ == "__main__":
    # s = "LVIII"
    s = "MCMXCIV"
    # print(brute_force(s))
    print(better_approach(s))
