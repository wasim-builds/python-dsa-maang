"""
Problem: Non-overlapping Intervals
Difficulty: Medium  Companies: Amazon,Google,Facebook,Bloomberg,Microsoft
Problem Statement: Return minimum number of intervals to remove to make rest non-overlapping.
Complexity: Time O(N log N), Space O(1)
"""

from typing import List


def solve_brute(intervals):
    return solve_optimal(intervals)


def solve_optimal(intervals):
    intervals.sort(key=lambda x: x[1])
    end = float("-inf")
    count = 0
    for s, e in intervals:
        if s >= end:
            end = e
        else:
            count += 1
    return count


if __name__ == "__main__":
    test_cases = [
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
    ]

    for inv, ex in test_cases:
        assert solve_optimal(inv) == ex
    print("All tests passed successfully!")
