"""
Problem: Longest Consecutive Sequence
Difficulty: Medium
Topic: 01_arrays
Companies: Google, Amazon, Microsoft, Facebook, Apple

Problem Statement:
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in `O(n)` time.

Complexity Proof:
- Time Complexity: O(N) because we insert all numbers into a hash set (O(N)), and then we only iterate through sequences starting from their lowest number. Each number is visited at most twice.
- Space Complexity: O(N) to store the hash set containing all the numbers.
"""

from typing import List


# BRUTE FORCE
# Time: O(N log N), Space: O(1) or O(N)
def solve_brute(nums: List[int]) -> int:
    if not nums:
        return 0

    nums.sort()
    longest = 1
    current = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            if nums[i] == nums[i - 1] + 1:
                current += 1
            else:
                longest = max(longest, current)
                current = 1

    return max(longest, current)


# OPTIMAL (Hash Set)
# Time: O(N), Space: O(N)
def solve_optimal(nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0

    for n in nums:
        # Check if it's the start of a sequence
        if (n - 1) not in numSet:
            length = 0
            while (n + length) in numSet:
                length += 1
            longest = max(longest, length)

    return longest


if __name__ == "__main__":
    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([], 0),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, expected in test_cases:
        assert solve_brute(nums) == expected
    print("All tests passed successfully!")
