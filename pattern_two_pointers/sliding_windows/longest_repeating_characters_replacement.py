"""
    Longest substring of repeating characters after replacement of letter with most k.
    LC Link: https://leetcode.com/problems/longest-repeating-character-replacement/description/

"""

import collections


def longest_repeating_characters(s: str, k: int) -> int:
    n = len(s)
    l = 0
    count_map = collections.Counter()
    longest_window = 0

    for r in range(n):
        right_elem = s[r]
        count_map[right_elem] += 1

        # Window valid check
        while (r-l+1) - max(count_map.values()) > k:
            left_elem = s[l]
            count_map[left_elem] -= 1
            if count_map[left_elem] == 0:
                del count_map[left_elem]
            l += 1

        current_window = r - l + 1
        longest_window = max(longest_window, current_window)
    
    return longest_window
        




if __name__ == "__main__":
    # s = "ABAB"; k = 2
    s = "AABABBA"; k = 1
    print(longest_repeating_characters(s, k))