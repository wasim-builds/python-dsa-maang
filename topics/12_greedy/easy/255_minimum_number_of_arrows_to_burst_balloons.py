"""
Problem: Minimum Number of Arrows to Burst Balloons
Difficulty: Easy  Companies: Microsoft,Amazon,Facebook
Problem Statement: Return minimum arrows needed to burst all balloons.
Complexity: Time O(N log N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(pts):
    return solve_optimal(pts)


def solve_optimal(points):
    points.sort(key=lambda x: x[1])
    arrows = 0
    end = float("-inf")
    for s, e in points:
        if s > end:
            arrows += 1
            end = e
    return arrows


@pytest.mark.parametrize(
    "pts,ex",
    [
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2]], 1),
    ],
)
def test_opt(pts, ex):
    assert solve_optimal(pts) == ex
