"""
Problem: Binary Search
Difficulty: Easy
Companies: Microsoft, Google, Apple

Problem Statement:
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Complexity Proof:
- Time Complexity: O(log N) because we halve the search space at every step.
- Space Complexity: O(1) because we only use two pointers (`l` and `r`) to define the search bounds.
"""

from typing import List


# OPTIMAL
# Time: O(log n), Space: O(1)
def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1

    while l <= r:
        m = l + ((r - l) // 2)  # prevents overflow
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m

    return -1


if __name__ == "__main__":
    test_cases = [([-1, 0, 3, 5, 9, 12], 9, 4), ([-1, 0, 3, 5, 9, 12], 2, -1)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, target, expected in test_cases:
        assert search(nums, target) == expected
    print("All tests passed successfully!")
