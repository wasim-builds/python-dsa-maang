"""
Problem #001: Two Sum
Difficulty: Easy
LeetCode: #1
Companies: Google ★★★, Amazon ★★★, Meta ★★★, Apple ★★★, Microsoft ★★★

Problem Statement:
    Given an array of integers nums and an integer target, return indices of
    the two numbers such that they add up to target.
    You may assume that each input would have exactly one solution.

Example:
    Input:  nums = [2,7,11,15], target = 9
    Output: [0,1]

Constraints:
    2 <= nums.length <= 10^4
    -10^9 <= nums[i] <= 10^9
    Only one valid answer exists.

Complexity Proof:
- Time Complexity: O(N) because we iterate through the list at most once. Hash map lookups take O(1) time on average.
- Space Complexity: O(N) because in the worst case, we might need to store N-1 elements in our hash map before finding a match.
"""

from typing import List
import pytest


# ═══════════════════════════════════════════════════════════
# APPROACH 1: BRUTE FORCE
# ═══════════════════════════════════════════════════════════
# Idea: Check every pair (i, j) where i < j
# Time:  O(n²)
# Space: O(1)
# ═══════════════════════════════════════════════════════════
def two_sum_brute(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


# ═══════════════════════════════════════════════════════════
# APPROACH 2: OPTIMAL — Hash Map (One Pass)
# ═══════════════════════════════════════════════════════════
# Idea: Store each number's index in a hash map.
#       For each num, check if (target - num) already exists.
# Time:  O(n)
# Space: O(n)
# ═══════════════════════════════════════════════════════════
def two_sum_optimal(nums: List[int], target: int) -> List[int]:
    seen = {}  # val -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# ═══════════════════════════════════════════════════════════
# TEST CASES
# ═══════════════════════════════════════════════════════════
@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum_optimal(nums, target, expected):
    assert two_sum_optimal(nums, target) == expected


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_two_sum_brute(nums, target, expected):
    assert two_sum_brute(nums, target) == expected
