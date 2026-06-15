"""
Problem: First Missing Positive
Difficulty: Hard
Topic: 01_arrays  Companies: Amazon,Microsoft,Apple,Bloomberg
Problem Statement: Given unsorted integer array, return smallest missing positive integer. Must be O(n) time and O(1) space.
Complexity: Time O(N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(nums):
    i = 1
    while i in nums:
        i += 1
    return i


def solve_optimal(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1


@pytest.mark.parametrize(
    "nums,ex", [([1, 2, 0], 3), ([3, 4, -1, 1], 2), ([7, 8, 9, 11, 12], 1)]
)
def test_opt(nums, ex):
    assert solve_optimal(nums[:]) == ex


@pytest.mark.parametrize("nums,ex", [([1, 2, 0], 3)])
def test_brute(nums, ex):
    assert solve_brute(nums) == ex
