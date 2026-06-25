"""
Problem: Combination Sum II
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Find all combinations of candidates summing to target, each number used once.
Complexity: Time O(2^N), Space O(N)
"""

from typing import List


def solve_brute(candidates, target):
    return solve_optimal(candidates, target)


def solve_optimal(candidates, target):
    candidates.sort()
    res = []

    def bt(i, comb, total):
        if total == target:
            res.append(comb[:])
            return
        if total > target or i >= len(candidates):
            return
        for j in range(i, len(candidates)):
            if j > i and candidates[j] == candidates[j - 1]:
                continue
            comb.append(candidates[j])
            bt(j + 1, comb, total + candidates[j])
            comb.pop()

    bt(0, [], 0)
    return res


if __name__ == "__main__":
    test_cases = [
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
    ]

    for c, t, ex in test_cases:
        assert sorted(solve_optimal(c, t)) == sorted(ex)
    print("All tests passed successfully!")
