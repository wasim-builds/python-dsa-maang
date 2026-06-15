"""
Problem: Permutations
Difficulty: Medium
Topic: 11_backtracking
Companies: Amazon, LinkedIn, Microsoft, Apple, Meta

Problem Statement:
Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

Complexity Proof:
- Time Complexity: O(N * N!) where N is the number of elements. There are N! permutations, and for each one we do O(N) work to copy it into the result list.
- Space Complexity: O(N) for the depth of the recursion stack.
"""

import pytest
from typing import List


# OPTIMAL (Backtracking DFS)
# Time: O(N * N!), Space: O(N)
def solve_optimal(nums: List[int]) -> List[List[int]]:
    res = []

    # Base case
    if len(nums) == 1:
        return [nums[:]]  # return a deep copy

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = solve_optimal(nums)

        for perm in perms:
            perm.append(n)
        res.extend(perms)

        nums.append(n)

    return res


# BRUTE FORCE / ALTERNATIVE (Iterative)
# Time: O(N * N!), Space: O(N * N!)
def solve_brute(nums: List[int]) -> List[List[int]]:
    perms = [[]]

    for n in nums:
        next_perms = []
        for p in perms:
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, n)
                next_perms.append(p_copy)
        perms = next_perms

    return perms


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    ],
)
def test_solve_optimal(nums, expected):
    result = solve_optimal(nums)
    assert sorted([tuple(x) for x in result]) == sorted([tuple(x) for x in expected])


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
    ],
)
def test_solve_brute(nums, expected):
    result = solve_brute(nums)
    assert sorted([tuple(x) for x in result]) == sorted([tuple(x) for x in expected])
