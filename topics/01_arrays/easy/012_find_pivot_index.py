"""
Problem: Find Pivot Index
Difficulty: Easy
Topic: 01_arrays
Companies: Amazon,Google

Problem Statement:
Find index where sum of left equals sum of right.

Complexity Proof:
- Time: O(N)
- Space: O(1)
"""

from typing import List


def solve_brute(nums):
    for i in range(len(nums)):
        if sum(nums[:i]) == sum(nums[i + 1 :]):
            return i
    return -1


def solve_optimal(nums):
    total = sum(nums)
    left = 0
    for i, n in enumerate(nums):
        if left == total - left - n:
            return i
        left += n
    return -1


if __name__ == "__main__":
    test_cases = [([1, 7, 3, 6, 5, 6], 3), ([1, 2, 3], -1)]

    for nums, expected in test_cases:
        assert solve_optimal(nums) == expected
    print("All tests passed successfully!")
