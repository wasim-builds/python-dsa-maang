"""
Problem: Subsets II
Difficulty: Easy  Companies: Amazon,Google,Meta
Problem Statement: Return all possible subsets of nums which may contain duplicates. No duplicate subsets.
Complexity: Time O(N * 2^N), Space O(N * 2^N)
"""

import pytest
from typing import List


def solve_brute(nums):
    return solve_optimal(nums)


def solve_optimal(nums):
    nums.sort()
    res = []

    def bt(i, subset):
        res.append(subset[:])
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue
            subset.append(nums[j])
            bt(j + 1, subset)
            subset.pop()

    bt(0, [])
    return res


@pytest.mark.parametrize(
    "nums,ex",
    [([1, 2, 2], [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]), ([0], [[], [0]])],
)
def test_opt(nums, ex):
    assert sorted(solve_optimal(nums)) == sorted(ex)
