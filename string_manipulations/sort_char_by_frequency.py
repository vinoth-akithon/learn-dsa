"""

"""


def brute_force(s: str) -> list[str]:
    """
        - Complexity Analysis:
            - Time -> O(n(for insertion) + 256(getting items as key value pair) + 256 * log 256 (sorting) + n(constructing output string))) ~= O(n)
            - Space -> O(256 (hash arr) + 2*256(key value pair) + 256 (sorting) + n(constructing output string)) ~= O(n)
    """
    # frequency counter
    hash_arr = [0] * 256
    for c in s:
        hash_arr[ord(c)] += 1

    # Removing non present char
    hash_arr = [(idx, val) for idx, val in enumerate(hash_arr) if val > 0]

    # stable sorting based on frequency (maintains the relative order)
    hash_arr = sorted(hash_arr, key=lambda x: -x[1])

    # forming the output sting
    res = ""
    for item in hash_arr:
        for _ in range(item[1]):
            res += chr(item[0])
    
    return res


if __name__ == "__main__":
    # s = "trffeeaA"
    # s = "raaaajj"
    s = "Aabb"
    print(brute_force(s))