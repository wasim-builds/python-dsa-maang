"""
Problem: Binary Search
Difficulty: Easy
Companies: Microsoft, Google, Apple

Problem Statement:
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List

# OPTIMAL
# Time: O(log n), Space: O(1)
def search(nums: List[int], target: int) -> int:
    l, r = 0, len(nums) - 1
    
    while l <= r:
        m = l + ((r - l) // 2) # prevents overflow
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
            
    return -1

if __name__ == "__main__":
    assert search([-1,0,3,5,9,12], 9) == 4
    assert search([-1,0,3,5,9,12], 2) == -1
    print("✅ All tests passed!")
