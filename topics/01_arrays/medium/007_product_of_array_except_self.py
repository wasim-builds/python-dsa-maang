"""
Problem: Product of Array Except Self
Difficulty: Medium
Companies: Amazon, Apple, Microsoft

Problem Statement:
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
You must write an algorithm that runs in O(n) time and without using the division operation.

Complexity Proof:
- Time Complexity: O(N) because we make two separate passes through the array (one for prefix, one for postfix).
- Space Complexity: O(1) because the output array does not count towards extra space complexity according to the problem statement. We only use constant extra variables.
"""

from typing import List
import pytest


# OPTIMAL
# Time: O(n), Space: O(1) (excluding output array)
def productExceptSelf(nums: List[int]) -> List[int]:
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ],
)
def test_productExceptSelf(nums, expected):
    assert productExceptSelf(nums) == expected
