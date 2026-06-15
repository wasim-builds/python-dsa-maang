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
    test_cases = [([1, 2, 3, 1], True), ([1, 2, 3, 4], False)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, expected in test_cases:
        assert containsDuplicate_brute(nums) == expected
    print("All tests passed successfully!")
