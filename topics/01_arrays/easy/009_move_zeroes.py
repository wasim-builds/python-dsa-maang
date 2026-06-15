"""
Problem: Move Zeroes
Difficulty: Easy
Topic: 01_arrays
Companies: Meta,Amazon

Problem Statement:
Move all 0s to end while maintaining relative order of non-zero elements.

Complexity Proof:
- Time: O(N)
- Space: O(1)
"""

from typing import List


def solve_brute(nums):
    nz = [x for x in nums if x != 0]
    nums[:] = nz + [0] * (len(nums) - len(nz))


def solve_optimal(nums):
    p = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[p], nums[i] = nums[i], nums[p]
            p += 1


if __name__ == "__main__":
    test_cases = [([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]), ([0], [0])]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, expected in test_cases:
        solve_optimal(nums)
        assert nums == expected
    print("All tests passed successfully!")
