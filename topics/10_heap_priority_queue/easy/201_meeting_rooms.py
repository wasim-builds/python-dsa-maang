"""
Problem: Meeting Rooms
Difficulty: Easy  Companies: Amazon,Google,Facebook,Microsoft
Problem Statement: Given meeting intervals, determine if person can attend all meetings.
Complexity: Time O(N log N), Space O(1)
"""

from typing import List


def solve_brute(intervals):
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


def solve_optimal(intervals):
    return solve_brute(intervals)


if __name__ == "__main__":
    test_cases = [([[0, 30], [5, 10], [15, 20]], False), ([[7, 10], [2, 4]], True)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for inv, ex in test_cases:
        assert solve_optimal(inv) == ex
    print("All tests passed successfully!")
