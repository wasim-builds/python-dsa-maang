"""
Problem: Capacity to Ship Packages Within D Days
Difficulty: Easy  Companies: Amazon,Google,Meta
Problem Statement: Find minimum weight capacity to ship all weights within D days.
Complexity: Time O(N log(sum-max)), Space O(1)
"""

from typing import List


def solve_brute(weights, days):
    l, r = max(weights), sum(weights)
    while l < r:
        mid = (l + r) // 2
        d = 1
        cur = 0
        for w in weights:
            if cur + w > mid:
                d += 1
                cur = 0
            cur += w
        if d <= days:
            r = mid
        else:
            l = mid + 1
    return l


def solve_optimal(weights, days):
    return solve_brute(weights, days)


if __name__ == "__main__":
    test_cases = [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5, 15), ([3, 2, 2, 4, 1, 4], 3, 6)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for w, d, ex in test_cases:
        assert solve_optimal(w, d) == ex
    print("All tests passed successfully!")
