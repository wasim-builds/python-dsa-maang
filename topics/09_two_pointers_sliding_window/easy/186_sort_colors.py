"""
Problem: Sort Colors
Difficulty: Easy  Companies: Microsoft,Amazon,Meta,Google
Problem Statement: Sort array with values 0,1,2 in-place using one pass (Dutch Flag).
Complexity: Time O(N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(nums):
    nums.sort()


def solve_optimal(nums):
    l = mid = 0
    r = len(nums) - 1
    while mid <= r:
        if nums[mid] == 0:
            nums[l], nums[mid] = nums[mid], nums[l]
            l += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[r] = nums[r], nums[mid]
            r -= 1
        else:
            mid += 1


@pytest.mark.parametrize(
    "nums,ex",
    [([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]), ([2, 0, 1], [0, 1, 2]), ([0], [0])],
)
def test_opt(nums, ex):
    solve_optimal(nums)
    assert nums == ex
