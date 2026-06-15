"""
Problem: Find Pivot Index
Difficulty: Easy
Topic: 01_arrays
Companies: Amazon,Google

Problem Statement:
Find index where sum of left equals sum of right.

Complexity Proof:
- Time: O(N)
- Space: O(1)
"""

import pytest
from typing import List


def solve_brute(nums):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1 :]):
            return i
    return -1


def solve_optimal(nums):
    total = sum(nums)
    left = 0
    for i, n in enumerate(nums):
        if left == total - left - n:
            return i
        left += n
    return -1


@pytest.mark.parametrize("nums,expected", [([1, 7, 3, 6, 5, 6], 3), ([1, 2, 3], -1)])
def test_optimal(nums, expected):
    assert solve_optimal(nums) == expected
