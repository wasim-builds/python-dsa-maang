"""
Problem: Meeting Rooms II
Difficulty: Medium  Companies: Amazon,Google,Facebook,Bloomberg,Microsoft
Problem Statement: Return minimum number of conference rooms required.
Complexity: Time O(N log N), Space O(N)
"""

import heapq
from typing import List


def solve_brute(intervals):
    intervals.sort()
    rooms = []
    for s, e in intervals:
        if rooms and rooms[0] <= s:
            heapq.heappop(rooms)
        heapq.heappush(rooms, e)
    return len(rooms)


def solve_optimal(intervals):
    return solve_brute(intervals)


if __name__ == "__main__":
    test_cases = [([[0, 30], [5, 10], [15, 20]], 2), ([[7, 10], [2, 4]], 1)]
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
