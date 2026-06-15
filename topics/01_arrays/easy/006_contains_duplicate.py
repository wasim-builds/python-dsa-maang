"""
Problem: Contains Duplicate
Difficulty: Easy
Topic: 01_arrays
Companies: Amazon,Google,Meta

Problem Statement:
Return true if any value appears at least twice.

Complexity Proof:
- Time: O(N)
- Space: O(N)
"""

import pytest
from typing import List


def solve_brute(nums):
    return len(nums) != len(set(nums))


def solve_optimal(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


@pytest.mark.parametrize("nums,expected", [([1, 2, 3, 1], True), ([1, 2, 3, 4], False)])
def test_optimal(nums, expected):
    assert solve_optimal(nums) == expected


@pytest.mark.parametrize("nums,expected", [([1, 2, 3, 1], True)])
def test_brute(nums, expected):
    assert solve_brute(nums) == expected
