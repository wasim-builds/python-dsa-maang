"""
Problem: Jump Game
Difficulty: Easy  Companies: Amazon,Google,Microsoft,Meta,Bloomberg
Problem Statement: Return true if can reach last index from first.
Complexity: Time O(N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(nums):
    reachable = 0
    for i in range(len(nums)):
        if i > reachable:
            return False
        reachable = max(reachable, i + nums[i])
    return True


def solve_optimal(nums):
    return solve_brute(nums)


@pytest.mark.parametrize("nums,ex", [([2, 3, 1, 1, 4], True), ([3, 2, 1, 0, 4], False)])
def test_opt(nums, ex):
    assert solve_optimal(nums) == ex
