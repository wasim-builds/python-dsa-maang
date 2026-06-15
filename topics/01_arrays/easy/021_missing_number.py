"""
Problem: Missing Number
Difficulty: Easy
Topic: 01_arrays
Companies: Amazon,Microsoft

Problem Statement:
Find the missing number in range [0,n].

Complexity Proof:
- Time: O(N)
- Space: O(1)
"""

import pytest
from typing import List


def solve_brute(nums):
    return [i for i in range(len(nums) + 1) if i not in nums][0]


def solve_optimal(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)


@pytest.mark.parametrize(
    "nums,expected", [([3, 0, 1], 2), ([0, 1], 2), ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8)]
)
def test_optimal(nums, expected):
    assert solve_optimal(nums) == expected
