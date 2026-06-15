"""
Problem: Subsets
Difficulty: Medium
Topic: 11_backtracking
Companies: Meta, Amazon, Bloomberg, Microsoft, Google

Problem Statement:
Given an integer array `nums` of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Complexity Proof:
- Time Complexity: O(N * 2^N) because there are 2^N possible subsets and for each subset, it takes O(N) to copy it to the output list.
- Space Complexity: O(N) for the DFS recursion stack to keep track of the current subset being built.
"""

from typing import List


# OPTIMAL (Backtracking DFS)
# Time: O(N * 2^N), Space: O(N)
def solve_optimal(nums: List[int]) -> List[List[int]]:
    res = []
    subset = []

    def dfs(i):
        if i >= len(nums):
            res.append(subset.copy())
            return

        # Decision to include nums[i]
        subset.append(nums[i])
        dfs(i + 1)

        # Decision NOT to include nums[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res


# BRUTE FORCE / ALTERNATIVE (Cascading Iterative)
# Time: O(N * 2^N), Space: O(N * 2^N)
def solve_brute(nums: List[int]) -> List[List[int]]:
    res = [[]]

    for num in nums:
        # For every existing subset, create a new one with the current number
        res += [curr + [num] for curr in res]

    return res


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for nums, expected in test_cases:
        result = solve_brute(nums)
        assert sorted([sorted(x) for x in result]) == sorted(
            [sorted(x) for x in expected]
        )
    print("All tests passed successfully!")
