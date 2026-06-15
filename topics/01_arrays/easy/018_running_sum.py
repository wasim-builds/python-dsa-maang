"""
Problem: Running Sum of 1D Array
Difficulty: Easy
Topic: 01_arrays
Companies: Amazon,Google

Problem Statement:
Return running sum where result[i] = sum(nums[0..i]).

Complexity Proof:
- Time: O(N)
- Space: O(N)
"""

import pytest
from typing import List


def solve_brute(nums):
    return [sum(nums[: i + 1]) for i in range(len(nums))]


def solve_optimal(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


@pytest.mark.parametrize(
    "nums,expected", [([1, 2, 3, 4], [1, 3, 6, 10]), ([1, 1, 1], [1, 2, 3])]
)
def test_optimal(nums, expected):
    assert solve_optimal(nums[:]) == expected
