"""
Problem: 3Sum
Difficulty: Medium
Topic: 01_arrays
Companies: Facebook, Amazon, Apple, Microsoft, Bloomberg

Problem Statement:
Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
Notice that the solution set must not contain duplicate triplets.

Complexity Proof:
- Time Complexity: O(N^2) where N is the length of the array. Sorting takes O(N log N) and the two-pointer loop takes O(N) for each of the N elements.
- Space Complexity: O(1) or O(N) depending on the sorting algorithm implementation. The output array does not count as extra space.
"""

from typing import List


# BRUTE FORCE
# Time: O(N^3), Space: O(1)
def solve_brute(nums: List[int]) -> List[List[int]]:
    res = set()
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.add(tuple(sorted((nums[i], nums[j], nums[k]))))
    return [list(x) for x in res]


# OPTIMAL
# Time: O(N^2), Space: O(1) or O(N)
def solve_optimal(nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res


if __name__ == "__main__":
    test_cases = [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for input_data, expected in test_cases:
        assert sorted([sorted(x) for x in solve_brute(input_data)]) == sorted(
            [sorted(x) for x in expected]
        )
    print("All tests passed successfully!")
