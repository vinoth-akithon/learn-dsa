"""

"""

def brute_force(s: str):
    """
        - Get all the odd integers and find the maximum among them.
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(n^2)
    """
    n = len(s)
    odds = []

    for i in range(n):
        if int(s[i]) == 0:
            continue

        for j in range(i, n):
            num = int(s[i:j+1])
            if num % 2 != 0:
                odds.append(num)

    return str(max(odds))


def optimal_approach(s: str):
    """
        - Traversing from right and check the current element is odd or not
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(s)

    for i in range(n):
        if s[i] != "0":
            s = s[i:]
            break

    n = len(s)
    for i in range(n-1, -1, -1):
        if int(s[i]) % 2 != 0:
            return s[:i+1]

    return ""


if __name__ == "__main__":
    s = "5347"
    s = "0214638"
    # print(brute_force(s))
    print(optimal_approach(s))