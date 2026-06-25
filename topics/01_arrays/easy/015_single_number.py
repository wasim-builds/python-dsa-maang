"""
Problem: Single Number
Difficulty: Easy
Topic: 01_arrays
Companies: Amazon,LeetCode

Problem Statement:
Every element appears twice except one. Find the single one using O(1) space.

Complexity Proof:
- Time: O(N)
- Space: O(1)
"""

from typing import List


def solve_brute(nums):
    from collections import Counter

    c = Counter(nums)
    return [k for k, v in c.items() if v == 1][0]


def solve_optimal(nums):
    r = 0
    for n in nums:
        r ^= n
    return r


if __name__ == "__main__":
    test_cases = [([2, 2, 1], 1), ([4, 1, 2, 1, 2], 4)]

    for nums, expected in test_cases:
        assert solve_optimal(nums) == expected
    print("All tests passed successfully!")
