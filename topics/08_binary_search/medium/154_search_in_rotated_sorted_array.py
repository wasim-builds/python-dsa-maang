"""
Problem: Search in Rotated Sorted Array
Difficulty: Medium
Topic: 08_binary_search
Companies: Meta, Amazon, Microsoft, LinkedIn, Apple

Problem Statement:
There is an integer array `nums` sorted in ascending order (with distinct values).
Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index.
Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.
You must write an algorithm with `O(log n)` runtime complexity.

Complexity Proof:
- Time Complexity: O(log N) because we halve the search space at every step using Binary Search.
- Space Complexity: O(1) because we only use two pointers (`l` and `r`).
"""

import pytest
from typing import List


# BRUTE FORCE
# Time: O(N), Space: O(1)
def solve_brute(nums: List[int], target: int) -> int:
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


# OPTIMAL (Binary Search)
# Time: O(log N), Space: O(1)
def solve_optimal(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid

        # Left sorted portion
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # Right sorted portion
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1

    return -1


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([5, 1, 3], 5, 0),
        ([5, 1, 3], 3, 2),
    ],
)
def test_solve_optimal(nums, target, expected):
    assert solve_optimal(nums, target) == expected


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([5, 1, 3], 5, 0),
        ([5, 1, 3], 3, 2),
    ],
)
def test_solve_brute(nums, target, expected):
    assert solve_brute(nums, target) == expected
