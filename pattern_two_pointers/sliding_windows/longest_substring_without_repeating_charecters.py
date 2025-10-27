def length_of_longest_substring(s: str) -> int:
        n = len(s)
        l = r = 0
        max_window = 1
        for i in range(1, n):
            if s[i] in s[l:r+1]:
                while s[l] != s[i]:
                    l += 1
                l += 1
                r += 1

            else:
                r += 1
            max_window = max(max_window, len(s[l:r+1]))
        return max_window

if __name__ == "__main__":
    s = "abcabcbb"
    # s = "bbbb"
    # s = "pwwkew"
    print(length_of_longest_substring(s))