"""
Problem: Wiggle Subsequence
Difficulty: Medium  Companies: Amazon,Google
Problem Statement: Return length of longest wiggle subsequence.
Complexity: Time O(N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(nums):
    return solve_optimal(nums)


def solve_optimal(nums):
    if len(nums) < 2:
        return len(nums)
    up = down = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up = down + 1
        elif nums[i] < nums[i - 1]:
            down = up + 1
    return max(up, down)


@pytest.mark.parametrize(
    "nums,ex",
    [
        ([1, 7, 4, 9, 2, 5], 6),
        ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2),
    ],
)
def test_opt(nums, ex):
    assert solve_optimal(nums) == ex
