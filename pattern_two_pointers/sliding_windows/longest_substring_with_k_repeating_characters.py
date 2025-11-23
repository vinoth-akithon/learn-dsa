"""
    Given string, find the length of the longest substring in it with no more than `K` unique charecters.
"""

import collections


def longest_substring_length(s: str, k: int) -> int:
    n = len(s)
    max_length = 0
    count_map = collections.Counter()
    l = 0

    for r in range(n):
        count_map[s[r]] += 1
        
        # Shrinking
        while len(count_map) > k:
            left_element = s[l]
            count_map[left_element] -= 1
            if count_map[left_element] == 0:
                del count_map[left_element]
            l += 1

        current_length = r - l + 1
        max_length = max(max_length, current_length)

    return max_length


if __name__ == "__main__":
    # s="araaci"; k=2
    # s="araaci"; k=1
    s="cbbebi"; k=3
    print(longest_substring_length(s, k))