"""
Problem: Combination Sum
Difficulty: Medium
Topic: 11_backtracking
Companies: Amazon, Microsoft, Meta, Airbnb, Apple

Problem Statement:
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may return the combinations in any order.
The same number may be chosen from `candidates` an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Complexity Proof:
- Time Complexity: O(N^(T/M)) where N is the number of candidates, T is the target, and M is the minimum value among the candidates. The recursion tree can go as deep as T/M.
- Space Complexity: O(T/M) for the recursion stack to store the current combination.
"""

from typing import List


# OPTIMAL (Backtracking DFS)
# Time: O(N^(T/M)), Space: O(T/M)
def solve_optimal(candidates: List[int], target: int) -> List[List[int]]:
    res = []

    def dfs(i, cur, total):
        if total == target:
            res.append(cur.copy())
            return
        if i >= len(candidates) or total > target:
            return

        # Decision 1: include candidates[i]
        cur.append(candidates[i])
        dfs(i, cur, total + candidates[i])

        # Decision 2: NOT include candidates[i]
        cur.pop()
        dfs(i + 1, cur, total)

    dfs(0, [], 0)
    return res


# BRUTE FORCE
# Brute force is fundamentally the same logic but without stopping at > target, which would run forever if we didn't cap it.
# The optimal backtracking DFS approach is the standard solution here.
def solve_brute(candidates: List[int], target: int) -> List[List[int]]:
    return solve_optimal(candidates, target)


if __name__ == "__main__":
    test_cases = [
        ([2, 3, 6, 7], 7, [[2, 2, 3], [7]]),
        ([2, 3, 5], 8, [[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        ([2], 1, []),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for candidates, target, expected in test_cases:
        result = solve_brute(candidates, target)
        assert sorted([sorted(x) for x in result]) == sorted(
            [sorted(x) for x in expected]
        )
    print("All tests passed successfully!")
