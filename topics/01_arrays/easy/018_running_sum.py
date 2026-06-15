"""
Problem: Running Sum of 1D Array
Difficulty: Easy
Topic: 01_arrays
Companies: Amazon,Google

Problem Statement:
Return running sum where result[i] = sum(nums[0..i]).

Complexity Proof:
- Time: O(N)
- Space: O(N)
"""

from typing import List


def solve_brute(nums):
    return [sum(nums[: i + 1]) for i in range(len(nums))]


def solve_optimal(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 4], [1, 3, 6, 10]), ([1, 1, 1], [1, 2, 3])]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, expected in test_cases:
        assert solve_optimal(nums[:]) == expected
    print("All tests passed successfully!")
