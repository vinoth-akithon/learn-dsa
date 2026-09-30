"""

"""

from collections import Counter


def brute_force(s: str, t: str):
    """
        - Using Auxiliary DS
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(2 * 256)
    """
    m = len(s)
    n = len(t)
    if m != n:
        return False

    hash_map = {}
    mapped_values = set()
    for i in range(n):
        char1 = s[i]
        char2 = t[i]
        if char1 in hash_map:
            if hash_map[char1] != char2:
                return False
        else:
            if char2 in mapped_values:
                return False
            hash_map[char1] = char2
            mapped_values.add(char2)
    return True


def optimal_approach(s: str, t: str) -> bool:
    """
        - Complexity Analysis:
            - Time -> O(n)
            - Space -> O(2* 256) ~= O(1)
    """
    s_arr = [0] * 256
    t_arr = [0] * 256
    m = len(s)

    for i in range(m):
        s_char = s[i]
        t_char = t[i]
        s_ord = ord(s_char)
        t_ord = ord(t_char)

        if s_arr[s_ord] == 0 and t_arr[t_ord] == 0:
            s_arr[s_ord] = t_ord+1
            t_arr[t_ord] = s_ord+1
        elif (s_arr[s_ord] != t_ord+1) or (t_arr[t_ord] != s_ord+1):
            return False
    return True

if __name__ == "__main__":
    # s = "paper"; t = "title"
    s = "foo"; t = "bar"
    print(brute_force(s, t))
    print(optimal_approach(s, t))