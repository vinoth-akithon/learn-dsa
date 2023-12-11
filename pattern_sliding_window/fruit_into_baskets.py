"""
    `This problem is same as longest substring with at most 2 distinct char`

    Given an array of characters where each character represents
    a fruit tree, you are given two baskets and your goal is to 
    put maximum number of fruits in each basket. 

    The only restriction is that each basket can have only one type of fruit.

    You can start with any tree, but once you have started you can't 
    skip a tree. You will pick one fruit from each tree until you cannot,
    i.e., you will stop when you have to pick from a third fruit type.

    Write a function to return the maximum number of fruits in both
    the baskets.

    Example 1:

    Input: Fruit=['A', 'B', 'C', 'A', 'C']
    Output: 3
    Explanation: We can put 2 'C' in one basket and one 'A' 
                in the other from the subarray ['C', 'A', 'C']
    
    Example 2:

    Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
    Output: 5
    Explanation: We can put 3 'B' in one basket and two 'C' in 
                the other basket. This can be done if we start 
                with the second letter: ['B', 'C', 'B', 'B', 'C']
"""
import unittest


def fruit_into_baskets(fruits: list[int]) -> int:
    window_start = 0
    fruit_frequency = {}
    max_length = 0

    for window_end in range(len(fruits)):
        try:
            fruit_frequency[fruits[window_end]] += 1
        except KeyError:
            fruit_frequency[fruits[window_end]] = 1

        while len(fruit_frequency) > 2:
            left_fruit = fruits[window_start]
            fruit_frequency[left_fruit] -= 1
            if fruit_frequency[left_fruit] == 0:
                fruit_frequency.pop(left_fruit)
            window_start += 1

        current_window_size = window_end + 1 - window_start
        if current_window_size > max_length:
            max_length = current_window_size

    return max_length


class TestCase(unittest.TestCase):
    def test_case1(self):
        return self.assertEqual(fruit_into_baskets(['A', 'B', 'C', 'A', 'C']), 3)

    def test_case2(self):
        return self.assertEqual(fruit_into_baskets(['A', 'B', 'C', 'B', 'B', 'C']), 5)


if __name__ == "__main__":
    # fruits = ['A', 'B', 'C', 'A', 'C']
    # print(fruit_into_baskets(fruits))
    unittest.main()
