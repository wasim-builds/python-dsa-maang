"""
Problem: Sum of All Subset XOR Totals
Difficulty: Medium  Companies: Amazon,Google
Problem Statement: Return sum of XOR totals for all subsets of nums.
Complexity: Time O(N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(nums):
    from itertools import combinations

    total = 0
    for r in range(len(nums) + 1):
        for combo in combinations(nums, r):
            xor = 0
            for n in combo:
                xor ^= n
            total += xor
    return total


def solve_optimal(nums):
    or_total = 0
    for n in nums:
        or_total |= n
    return or_total * (1 << (len(nums) - 1))


@pytest.mark.parametrize(
    "nums,ex", [([1, 3], 6), ([5, 1, 6], 28), ([3, 4, 5, 6, 7, 8], 480)]
)
def test_opt(nums, ex):
    assert solve_optimal(nums) == ex


@pytest.mark.parametrize("nums,ex", [([1, 3], 6)])
def test_brute(nums, ex):
    assert solve_brute(nums) == ex
