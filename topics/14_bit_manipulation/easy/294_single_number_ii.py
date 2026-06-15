"""
Problem: Single Number II
Difficulty: Easy  Companies: Amazon,Google,Bloomberg
Problem Statement: Find element appearing once; all others appear three times. O(1) space.
Complexity: Time O(N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(nums):
    from collections import Counter

    return [k for k, v in Counter(nums).items() if v == 1][0]


def solve_optimal(nums):
    ones = twos = 0
    for n in nums:
        ones = (ones ^ n) & ~twos
        twos = (twos ^ n) & ~ones
    return ones


@pytest.mark.parametrize("nums,ex", [([2, 2, 3, 2], 3), ([0, 1, 0, 1, 0, 1, 99], 99)])
def test_opt(nums, ex):
    assert solve_optimal(nums) == ex
