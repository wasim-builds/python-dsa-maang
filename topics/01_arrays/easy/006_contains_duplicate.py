"""
Problem: Contains Duplicate
Difficulty: Easy
Topic: 01_arrays
Companies: Amazon,Google,Meta

Problem Statement:
Return true if any value appears at least twice.

Complexity Proof:
- Time: O(N)
- Space: O(N)
"""

from typing import List


def solve_brute(nums):
    return len(nums) != len(set(nums))


def solve_optimal(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 1], True)]

    for nums, expected in test_cases:
        assert solve_brute(nums) == expected
    print("All tests passed successfully!")
