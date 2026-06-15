"""
Problem: House Robber
Difficulty: Medium
Topic: 07_dynamic_programming
Companies: Google, Amazon, Microsoft, Meta, Apple

Problem Statement:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Complexity Proof:
- Time Complexity: O(N) where N is the number of houses. We iterate through the array exactly once.
- Space Complexity: O(1) because we only need to keep track of the max loot from the last two houses (`rob1` and `rob2`) rather than maintaining a full DP array.
"""

import pytest
from typing import List


# BRUTE FORCE / ALTERNATIVE (Recursive DFS with Memoization)
# Time: O(N), Space: O(N)
def solve_brute(nums: List[int]) -> int:
    memo = {}

    def dfs(i):
        if i >= len(nums):
            return 0
        if i in memo:
            return memo[i]

        memo[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
        return memo[i]

    return dfs(0)


# OPTIMAL (Bottom-Up DP with Space Optimization)
# Time: O(N), Space: O(1)
def solve_optimal(nums: List[int]) -> int:
    rob1, rob2 = 0, 0

    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp

    return rob2


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([0], 0),
    ],
)
def test_solve_optimal(nums, expected):
    assert solve_optimal(nums) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
        ([0], 0),
    ],
)
def test_solve_brute(nums, expected):
    assert solve_brute(nums) == expected
