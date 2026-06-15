"""
Problem: Minimum Number of Arrows to Burst Balloons
Difficulty: Easy  Companies: Microsoft,Amazon,Facebook
Problem Statement: Return minimum arrows needed to burst all balloons.
Complexity: Time O(N log N), Space O(1)
"""

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


if __name__ == "__main__":
    test_cases = [
        ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
        ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
        ([[1, 2]], 1),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for pts, ex in test_cases:
        assert solve_optimal(pts) == ex
    print("All tests passed successfully!")
