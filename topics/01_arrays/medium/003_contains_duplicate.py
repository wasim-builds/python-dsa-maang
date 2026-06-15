"""
Problem: Contains Duplicate
Difficulty: Easy
Companies: Apple, Amazon, Microsoft

Problem Statement:
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Complexity Proof:
- Time Complexity: O(N) because creating a set from an array of N elements requires iterating through every element once.
- Space Complexity: O(N) because the set can grow up to the size of the array if all elements are distinct.
"""

from typing import List
import pytest


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


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
    ],
)
def test_containsDuplicate_optimal(nums, expected):
    assert containsDuplicate_optimal(nums) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
    ],
)
def test_containsDuplicate_brute(nums, expected):
    assert containsDuplicate_brute(nums) == expected
