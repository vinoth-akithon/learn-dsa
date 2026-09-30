"""
Given two strings, check whether two strings are anagrams of each other
"""

from collections import Counter

def brute_force(s: str, t: str) -> bool:
    """
        - Sort the both the string and then compare
        - Complexity Analysis:
            - Time -> O(2n log n + n)
            - Space -> O(2n)
    """
    m = len(s)
    n = len(t)

    if m != n:
        return False

    s = sorted(s)
    t = sorted(t)

    return s == t
    


def optimal_approach(s: str, t: str) -> bool:
    """
        - Getting the frequency of two strings and compare both are matches
        - Complexity Analysis:
            - Time -> O(3n) 
            - Space -> O(2*26) ~= O(1)
    """
    m = len(s)
    n = len(t)
    if m != n:
        return False
    
    s_map = Counter(s)
    t_map = Counter(t)

    return s_map == t_map


if __name__ == "__main__":
    s = "cat"; t = "act"
    # s = "rules"; t = "lesrt"
    print(brute_force(s, t))
