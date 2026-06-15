"""
Problem: Minimum Size Subarray Sum
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Return min length subarray with sum >= target. Return 0 if none.
Complexity: Time O(N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(target, nums):
    n = len(nums)
    res = float("inf")
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            if s >= target:
                res = min(res, j - i + 1)
                break
    return 0 if res == float("inf") else res


def solve_optimal(target, nums):
    l = total = 0
    res = float("inf")
    for r in range(len(nums)):
        total += nums[r]
        while total >= target:
            res = min(res, r - l + 1)
            total -= nums[l]
            l += 1
    return 0 if res == float("inf") else res


@pytest.mark.parametrize(
    "t,nums,ex",
    [(7, [2, 3, 1, 2, 4, 3], 2), (4, [1, 4, 4], 1), (11, [1, 1, 1, 1, 1, 1, 1, 1], 0)],
)
def test_opt(t, nums, ex):
    assert solve_optimal(t, nums) == ex
