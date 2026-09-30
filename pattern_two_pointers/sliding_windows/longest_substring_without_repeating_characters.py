# def length_of_longest_substring(s: str) -> int:
#         n = len(s)
#         l = r = 0
#         max_window = 1
#         for i in range(1, n):
#             if s[i] in s[l:r+1]:
#                 while s[l] != s[i]:
#                     l += 1
#                 l += 1
#                 r += 1

#             else:
#                 r += 1
#             max_window = max(max_window, len(s[l:r+1]))
#         return max_window


def brute_force_approch(s: str) -> int:
    n = len(s)
    max_length = 0
    for i in range(n):
        substring = ""
        for j in range(i, n):
            if s[j] in substring:
                break
            else:
                substring += s[j]
                if (len(substring) > max_length):
                    max_length = len(substring)
    return max_length

import collections


def length_of_longest_substring(s: str) -> int:
    n = len(s)
    l = 0
    counter = collections.Counter()
    max_window = 0
    for r in range(n):
        counter[s[r]] += 1

        while (len(counter) < (r-l+1)):
            left_elem = s[l]
            counter[left_elem] -= 1
            if counter[left_elem] == 0:
                del counter[left_elem]
            l += 1
            
        max_window = max(max_window, r-l+1)
    return max_window

if __name__ == "__main__":
    s = "abcabcbb"
    # s = "bbbb"
    # s = "pwwkew"
    # print(length_of_longest_substring(s))
    print(brute_force_approch(s))