"""
    Given a string, find the length of the longest substring
    which has no repeating characters.

    Example 1:
    -----------
    Input: String="aabccbb"
    Output: 3
    Explanation: The longest substring without any repeating characters is "abc".
    
    Example 2:
    -----------
    Input: String="abbbb"
    Output: 2
    Explanation: The longest substring without any repeating characters is "ab".
    
    Example 3:
    -----------
    Input: String="abccde"
    Output: 3
    Explanation: Longest substrings without any repeating characters are "abc" & "cde".

    Time Complexity: O(N)

    Space Complexity: O(K) K distinct char in hashmap(at worse case k<=N)
                    If the input string is fixed like only alphabet, we can 
                    say the algorithm run in O(1) because we can use `fized size 
                    array` instead of `hashmap`
"""
import unittest
import timeit


def longest_substring_with_no_repeat_char2(S: str):
    start = 0
    max_length = 0
    hash_table = {}
    for end in range(len(S)):
        presented_index = hash_table.get(S[end], None)
        if presented_index is not None and presented_index >= start:
            start = presented_index + 1

        hash_table[S[end]] = end

        current_window_size = end + 1 - start
        if current_window_size > max_length:
            max_length = current_window_size

    return max_length


class TestCase(unittest.TestCase):
    def test_case1(self):
        return self.assertEqual(longest_substring_with_no_repeat_char2("aabccbb"), 3)

    def test_case2(self):
        return self.assertEqual(longest_substring_with_no_repeat_char2("abbbb"), 2)

    def test_case3(self):
        return self.assertEqual(longest_substring_with_no_repeat_char2("abccde"), 3)


if __name__ == "__main__":
    # unittest.main()
    # print(timeit.timeit("longest_substring_with_no_repeat_char('aabccbb')",
    #                     setup="from __main__ import longest_substring_with_no_repeat_char"))
    # print(timeit.timeit("longest_substring_with_no_repeat_char2('aabccbb')",
    # setup="from __main__ import longest_substring_with_no_repeat_char2"))

    print(longest_substring_with_no_repeat_char2("abba"))
