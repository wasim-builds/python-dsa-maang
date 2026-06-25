"""
Problem: Maximum Product Subarray
Difficulty: Medium
Topic: 07_dynamic_programming
Companies: LinkedIn, Amazon, Google, Meta, Microsoft

Problem Statement:
Given an integer array `nums`, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.

Complexity Proof:
- Time Complexity: O(N) because we iterate through the array exactly once, keeping track of the running maximum and minimum products.
- Space Complexity: O(1) because we only need to store `res`, `curMax`, and `curMin`.
"""

from typing import List


# BRUTE FORCE
# Time: O(N^2), Space: O(1)
def solve_brute(nums: List[int]) -> int:
    res = nums[0]
    for i in range(len(nums)):
        cur = 1
        for j in range(i, len(nums)):
            cur *= nums[j]
            res = max(res, cur)
    return res


# OPTIMAL (Kadane's Algorithm variation)
# Time: O(N), Space: O(1)
def solve_optimal(nums: List[int]) -> int:
    res = max(nums)
    curMin, curMax = 1, 1

    for n in nums:
        # If we hit a 0, the current streak is broken, reset mins/maxes
        if n == 0:
            curMin, curMax = 1, 1
            continue

        temp = curMax * n
        # Because multiplying two negatives makes a positive, we must track the curMin as well
        curMax = max(temp, n * curMin, n)
        curMin = min(temp, n * curMin, n)

        res = max(res, curMax)

    return res


if __name__ == "__main__":
    test_cases = [([2, 3, -2, 4], 6), ([-2, 0, -1], 0), ([-2, 3, -4], 24)]

    for nums, expected in test_cases:
        assert solve_brute(nums) == expected
    print("All tests passed successfully!")
