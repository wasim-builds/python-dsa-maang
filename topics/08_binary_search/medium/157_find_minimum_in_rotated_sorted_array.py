"""
Problem: Find Minimum in Rotated Sorted Array
Difficulty: Medium
Topic: 08_binary_search
Companies: Microsoft, Amazon, Meta, Bloomberg, Apple

Problem Statement:
Suppose an array of length `n` sorted in ascending order is rotated between `1` and `n` times.
Given the sorted rotated array `nums` of unique elements, return the minimum element of this array.
You must write an algorithm that runs in `O(log n)` time.

Complexity Proof:
- Time Complexity: O(log N) because we halve the search space during every iteration of our binary search.
- Space Complexity: O(1) because we only use two pointers (`l` and `r`) to find the minimum.
"""

from typing import List


# BRUTE FORCE
# Time: O(N), Space: O(1)
def solve_brute(nums: List[int]) -> int:
    return min(nums)


# OPTIMAL (Binary Search)
# Time: O(log N), Space: O(1)
def solve_optimal(nums: List[int]) -> int:
    res = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break

        mid = (l + r) // 2
        res = min(res, nums[mid])

        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1

    return res


if __name__ == "__main__":
    test_cases = [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
    ]

    for nums, expected in test_cases:
        assert solve_brute(nums) == expected
    print("All tests passed successfully!")
