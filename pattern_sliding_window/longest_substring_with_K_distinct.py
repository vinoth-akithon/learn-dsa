"""
    Given a string, find the length of the longest substring
    in it with no more than K distinct characters.

    Example 1:
        Input: String="araaci", K=2
        Output: 4
        Explanation: The longest substring with no more than 
                    '2' distinct characters is "araa".
    
    Example 2:
        Input: String="araaci", K=1
        Output: 2
        Explanation: The longest substring with no more than 
                    '1' distinct characters is "aa".
    
    Example 3:
        Input: String="cbbebi", K=3
        Output: 5
        Explanation: The longest substrings with no more than 
                    '3' distinct characters are "cbbeb" & "bbebi".

                    
    Time Complexity: O(N + N) = O(N) 
    Space Complexity: O(K+1) = O(K) due to Hashmap 
"""
import unittest


def longest_substring_with_K_distinct(input_str, K):
    max_length = 0
    start_window = 0
    hash_map = {}
    for end_window in range(len(input_str)):
        # max_length += 1
        try:
            hash_map[input_str[end_window]] += 1
        except KeyError:
            hash_map[input_str[end_window]] = 1

        while len(hash_map) > K:
            left_char = input_str[start_window]
            hash_map[left_char] -= 1
            if hash_map[left_char] == 0:
                hash_map.pop(left_char)
            start_window += 1
        max_length = max(max_length, end_window-start_window+1)
    return max_length


class TestLongest(unittest.TestCase):
    def test_case1(self):
        return self.assertEqual(longest_substring_with_K_distinct("araaci", 2), 4)

    def test_case2(self):
        return self.assertEqual(longest_substring_with_K_distinct("araaci", 1), 2)

    def test_case3(self):
        return self.assertEqual(longest_substring_with_K_distinct("cbbebi", 3), 5)


if __name__ == "__main__":
    # print(longest_substring_with_K_distinct("araaci", 2))
    unittest.main()
