"""

"""
from collections import Counter, defaultdict

def brute_force(s: str, k: int):
    """
        - Complexity Analysis:
            - Time -> O(n^2)
            - Space -> O(1)
    """
    cnt = 0
    n = len(s)
    for i in range(n):
        counter = defaultdict(int)
        for j in range(i, n):
            counter[s[j]] += 1
            if len(counter) == k:
                cnt += 1
            elif len(counter) > k:
                break

    return cnt


def at_most_k_distinct(s: str, k: int):
    """
        - Using sliding window
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(1)
    """
    n = len(s)
    l = r = 0
    cnt = 0
    hash_map = defaultdict(int)

    while (r < n):
        hash_map[s[r]] += 1

        while len(hash_map) > k:
            hash_map[s[l]] -= 1
            if not hash_map[s[l]]:
                del hash_map[s[l]]
            l += 1

        # no of valid substring at ending at right (start from anywhere in the range)
        cnt += r - l + 1
        r += 1

    return cnt


def optimal_approach(s: str, k: int):
    return at_most_k_distinct(s, k) - at_most_k_distinct(s, k-1)


if __name__ == "__main__":
    s = "pqpqs"; k = 2  
    print(brute_force(s, k))
    print(optimal_approach(s, k))


