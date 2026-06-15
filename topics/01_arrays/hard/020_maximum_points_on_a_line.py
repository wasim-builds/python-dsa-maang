"""
Problem: Max Points on a Line
Difficulty: Hard
Topic: 01_arrays  Companies: Amazon,LinkedIn,Twitter
Problem Statement: Given array of points, return max number of points that lie on the same straight line.
Complexity: Time O(N^2), Space O(N)
"""

import pytest
from typing import List
from collections import defaultdict
from math import gcd


def solve_brute(points):
    if len(points) <= 2:
        return len(points)
    res = 2
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            cnt = 2
            x1, y1 = points[i]
            x2, y2 = points[j]
            for k in range(len(points)):
                if k == i or k == j:
                    continue
                x3, y3 = points[k]
                if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
                    cnt += 1
            res = max(res, cnt)
    return res


def solve_optimal(points):
    if len(points) <= 2:
        return len(points)
    res = 2
    for i in range(len(points)):
        slopes = defaultdict(int)
        for j in range(i + 1, len(points)):
            dy = points[j][1] - points[i][1]
            dx = points[j][0] - points[i][0]
            g = gcd(abs(dy), abs(dx))
            if g:
                dy, dx = dy // g, dx // g
            if dx < 0:
                dy, dx = -dy, -dx
            elif dx == 0:
                dy = 1
            slopes[(dy, dx)] += 1
        if slopes:
            res = max(res, max(slopes.values()) + 1)
    return res


@pytest.mark.parametrize(
    "pts,ex",
    [
        ([[1, 1], [2, 2], [3, 3]], 3),
        ([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]], 4),
    ],
)
def test_opt(pts, ex):
    assert solve_optimal(pts) == ex


@pytest.mark.parametrize("pts,ex", [([[1, 1], [2, 2], [3, 3]], 3)])
def test_brute(pts, ex):
    assert solve_brute(pts) == ex
