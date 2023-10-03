"""
Concatenation of Array

Given an integer array nums of length n, 
you want to create an array ans of length 2n
where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans


Example 1:
    Input: nums = [1,2,1]
    Output: [1,2,1,1,2,1]

Example 2:
    Input: nums = [1,3,2,1]
    Output: [1,3,2,1,1,3,2,1]
"""


def concatinate(nums: list[int]) -> list[int]:
    length = len(nums)
    for i in range(length):
        nums.append(nums[i])
    return nums

if __name__ == '__main__':
    # arr = [1,2,1]
    arr = [1,3,2,1]
    print(concatinate(arr))