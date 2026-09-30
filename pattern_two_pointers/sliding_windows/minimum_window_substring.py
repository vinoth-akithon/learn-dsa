import collections


def optimal_approch(s: str, t: str) -> str:
    m = len(s)

    need = collections.Counter(t)
    have = {}
    required = len(need)
    formed = 0
    min_window = float("inf")
    min_window_subarray = ""
    l = 0

    for r in range(m):
        right_elem = s[r]
        have[right_elem] = have.get(right_elem, 0) + 1

        if right_elem in need and need[right_elem] == have[right_elem]:
            formed += 1
        
        while formed == required:
            if r-l+1 < min_window:
                min_window = r-l+1
                min_window_subarray = s[l:r+1]

            # shrinking
            have[s[l]] -= 1
            if s[l] in need and have[s[l]] < need[s[l]]:
                formed -= 1
            l += 1
    return min_window_subarray




if __name__ == "__main__":
    s = "ADOBECODEBANC"; t = "ABC"
    # s = "a"; t = "a"
    # s = "a"; t = "aa"
    print(optimal_approch(s, t))