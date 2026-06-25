"""
Problem: Maximum Subarray (Kadane's Algorithm)
Difficulty: Medium
Companies: Amazon, Microsoft, LinkedIn, Google

Problem Statement:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Complexity Proof:
- Time Complexity: O(N) because we iterate through the array of numbers exactly once, performing O(1) operations at each step.
- Space Complexity: O(1) because we only maintain two variables (`max_sum` and `curr_sum`).
"""

from typing import List


# BRUTE FORCE
# Time: O(n^2), Space: O(1)
def maxSubArray_brute(nums: List[int]) -> int:
    max_sum = float("-inf")
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum


# OPTIMAL (Kadane's Algorithm)
# Time: O(n), Space: O(1)
def maxSubArray_optimal(nums: List[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0
    for n in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += n
        max_sum = max(max_sum, curr_sum)
    return max_sum


if __name__ == "__main__":
    test_cases = [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
    ]

    for nums, expected in test_cases:
        assert maxSubArray_brute(nums) == expected
    print("All tests passed successfully!")
