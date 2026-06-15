"""
Problem: Max Points on a Line
Difficulty: Hard
Topic: 01_arrays  Companies: Amazon,LinkedIn,Twitter
Problem Statement: Given array of points, return max number of points that lie on the same straight line.
Complexity: Time O(N^2), Space O(N)
"""

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


if __name__ == "__main__":
    test_cases = [([[1, 1], [2, 2], [3, 3]], 3)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for pts, ex in test_cases:
        assert solve_brute(pts) == ex
    print("All tests passed successfully!")
