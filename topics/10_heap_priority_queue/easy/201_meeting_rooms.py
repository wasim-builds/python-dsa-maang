"""
Problem: Meeting Rooms
Difficulty: Easy  Companies: Amazon,Google,Facebook,Microsoft
Problem Statement: Given meeting intervals, determine if person can attend all meetings.
Complexity: Time O(N log N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(intervals):
    intervals.sort()
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True


def solve_optimal(intervals):
    return solve_brute(intervals)


@pytest.mark.parametrize(
    "inv,ex", [([[0, 30], [5, 10], [15, 20]], False), ([[7, 10], [2, 4]], True)]
)
def test_opt(inv, ex):
    assert solve_optimal(inv) == ex
