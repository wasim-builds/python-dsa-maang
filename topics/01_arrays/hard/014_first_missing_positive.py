"""
Problem: First Missing Positive
Difficulty: Hard
Topic: 01_arrays  Companies: Amazon,Microsoft,Apple,Bloomberg
Problem Statement: Given unsorted integer array, return smallest missing positive integer. Must be O(n) time and O(1) space.
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(nums):
    i = 1
    while i in nums:
        i += 1
    return i


def solve_optimal(nums):
    n = len(nums)
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1


if __name__ == "__main__":
    test_cases = [([1, 2, 0], 3)]

    for nums, ex in test_cases:
        assert solve_brute(nums) == ex
    print("All tests passed successfully!")
