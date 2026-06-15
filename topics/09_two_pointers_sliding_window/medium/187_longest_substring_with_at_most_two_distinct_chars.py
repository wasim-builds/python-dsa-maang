"""
Problem: Fruit Into Baskets (Longest Subarray with At Most 2 Distinct)
Difficulty: Medium  Companies: Amazon,Google,Facebook
Problem Statement: Find longest subarray with at most 2 distinct values.
Complexity: Time O(N), Space O(1)
"""

from typing import List


def solve_brute(fruits):
    res = 0
    for i in range(len(fruits)):
        seen = set()
        for j in range(i, len(fruits)):
            seen.add(fruits[j])
            if len(seen) > 2:
                break
            res = max(res, j - i + 1)
    return res


def solve_optimal(fruits):
    count = {}
    l = res = 0
    for r in range(len(fruits)):
        count[fruits[r]] = count.get(fruits[r], 0) + 1
        while len(count) > 2:
            count[fruits[l]] -= 1
            if count[fruits[l]] == 0:
                del count[fruits[l]]
            l += 1
        res = max(res, r - l + 1)
    return res


if __name__ == "__main__":
    test_cases = [([1, 2, 1], 3), ([0, 1, 2, 2], 3), ([1, 2, 3, 2, 2], 4)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for f, ex in test_cases:
        assert solve_optimal(f) == ex
    print("All tests passed successfully!")
