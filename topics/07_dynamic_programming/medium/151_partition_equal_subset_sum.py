"""
Problem: Partition Equal Subset Sum
Difficulty: Medium  Companies: Amazon,Google,Meta,Microsoft
Problem Statement: Partition array into two subsets with equal sum.
Complexity: Time O(N * sum/2), Space O(sum/2)
"""

import pytest
from typing import List


def solve_brute(nums):
    target = sum(nums)
    if target % 2:
        return False
    target //= 2
    dp = {0}
    for n in nums:
        dp |= {s + n for s in dp}
    return target in dp


def solve_optimal(nums):
    return solve_brute(nums)


@pytest.mark.parametrize("nums,ex", [([1, 5, 11, 5], True), ([1, 2, 3, 5], False)])
def test_opt(nums, ex):
    assert solve_optimal(nums) == ex
