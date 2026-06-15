"""
Problem: Meeting Rooms II
Difficulty: Medium  Companies: Amazon,Google,Facebook,Bloomberg,Microsoft
Problem Statement: Return minimum number of conference rooms required.
Complexity: Time O(N log N), Space O(N)
"""

import pytest, heapq
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


@pytest.mark.parametrize(
    "inv,ex", [([[0, 30], [5, 10], [15, 20]], 2), ([[7, 10], [2, 4]], 1)]
)
def test_opt(inv, ex):
    assert solve_optimal(inv) == ex
