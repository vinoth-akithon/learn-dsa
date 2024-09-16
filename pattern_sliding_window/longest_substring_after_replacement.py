"""
    Given a string with lowercase letters only, if you are allowed
    to replace no more than `k` letters with any letter, 
    find the length of the longest substring having the same 
    letters after replacement.

    Example 1:
    ------------
    Input: String="aabccbb", k=2
    Output: 5
    Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
    
    Example 2:
    ------------
    Input: String="abbcb", k=1
    Output: 4
    Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
    
    Example 3:
    -----------
    Input: String="abccde", k=1
    Output: 3
    Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".
"""

from collections import defaultdict
import unittest
import timeit


def longest_subscript_after_replacement(S: str, K: int) -> int:
    start = 0
    max_length = 0
    max_repeated_char_count = 0
    hash_table = defaultdict(int)

    for end in range(len(S)):
        right_char = S[end]
        hash_table[right_char] += 1
        if max_repeated_char_count < hash_table[right_char]:
            max_repeated_char_count = hash_table[right_char]

        if (end + 1 - start - max_repeated_char_count) > K:
            left_char = S[start]
            hash_table[left_char] -= 1
            if hash_table[left_char] == 0:
                hash_table.pop(left_char)
            start += 1

            max_repeated_char_count = max(hash_table.values(), default=0)

        max_length = max(max_length, end + 1 - start)

    return max_length


class TestCase(unittest.TestCase):
    def test_case1(self):
        return self.assertEqual(
            longest_subscript_after_replacement("aabccbb", 2), 5)

    def test_case2(self):
        return self.assertEqual(
            longest_subscript_after_replacement("abbcb", 1), 4)

    def test_case3(self):
        return self.assertEqual(
            longest_subscript_after_replacement("abccde", 1), 3)


if __name__ == "__main__":
    unittest.main()
    # print(longest_subscript_after_replacement("AABABBA", 1))
    # print(timeit.timeit("longest_subscript_after_replacement('aabccbb', 2)",
    #                     setup="from __main__ import longest_subscript_after_replacement"))
