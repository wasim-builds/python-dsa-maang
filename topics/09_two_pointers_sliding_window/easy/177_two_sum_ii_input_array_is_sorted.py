"""
Problem: Two Sum II - Input Array is Sorted
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Find two numbers in sorted array summing to target. Return 1-indexed.
Complexity: Time O(N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]


def solve_optimal(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        elif s < target:
            l += 1
        else:
            r -= 1


@pytest.mark.parametrize(
    "nums,t,ex",
    [([2, 7, 11, 15], 9, [1, 2]), ([2, 3, 4], 6, [1, 3]), ([3, 3], 6, [1, 2])],
)
def test_opt(nums, t, ex):
    assert solve_optimal(nums, t) == ex
