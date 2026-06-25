"""
Problem: Max Consecutive Ones III
Difficulty: Medium
Topic: 01_arrays  Companies: Google,Amazon,Meta
Problem Statement: Return max number of consecutive 1s if you can flip at most k zeros.
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(nums, k):
    res = 0
    for i in range(len(nums)):
        zeros = 0
        for j in range(i, len(nums)):
            if nums[j] == 0:
                zeros += 1
            if zeros > k:
                break
            res = max(res, j - i + 1)
    return res


def solve_optimal(nums, k):
    l = zeros = res = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            zeros += 1
        while zeros > k:
            if nums[l] == 0:
                zeros -= 1
            l += 1
        res = max(res, r - l + 1)
    return res


if __name__ == "__main__":
    test_cases = [([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2, 6)]

    for nums, k, ex in test_cases:
        assert solve_brute(nums, k) == ex
    print("All tests passed successfully!")
