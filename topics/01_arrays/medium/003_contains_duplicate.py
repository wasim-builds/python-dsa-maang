"""
Problem: Contains Duplicate
Difficulty: Easy
Companies: Apple, Amazon, Microsoft

Problem Statement:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
from typing import List

# BRUTE FORCE
# Time: O(n^2), Space: O(1)
def containsDuplicate_brute(nums: List[int]) -> bool:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# OPTIMAL
# Time: O(n), Space: O(n)
def containsDuplicate_optimal(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)

if __name__ == "__main__":
    assert containsDuplicate_optimal([1,2,3,1]) == True
    assert containsDuplicate_optimal([1,2,3,4]) == False
    print("✅ All tests passed!")
