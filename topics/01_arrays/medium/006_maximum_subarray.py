"""
Problem: Maximum Subarray (Kadane's Algorithm)
Difficulty: Medium
Companies: Amazon, Microsoft, LinkedIn, Google

Problem Statement:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
"""
from typing import List

# BRUTE FORCE
# Time: O(n^2), Space: O(1)
def maxSubArray_brute(nums: List[int]) -> int:
    max_sum = float('-inf')
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
    assert maxSubArray_optimal([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert maxSubArray_optimal([1]) == 1
    assert maxSubArray_optimal([5,4,-1,7,8]) == 23
    print("✅ All tests passed!")
