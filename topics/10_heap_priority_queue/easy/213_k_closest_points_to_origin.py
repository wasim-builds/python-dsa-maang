"""
Problem: K Closest Points to Origin
Difficulty: Easy  Companies: Amazon,Google,Meta,Facebook
Problem Statement: Return k closest points to origin.
Complexity: Time O(N log k), Space O(k)
"""

import heapq
from typing import List


def solve_brute(points, k):
    return sorted(points, key=lambda p: p[0] ** 2 + p[1] ** 2)[:k]


def solve_optimal(points, k):
    heap = []
    for x, y in points:
        heapq.heappush(heap, (-(x * x + y * y), x, y))
        if len(heap) > k:
            heapq.heappop(heap)
    return [[x, y] for _, x, y in heap]


if __name__ == "__main__":
    test_cases = [([[1, 3], [-2, 2]], 1), ([[3, 3], [5, -1], [-2, 4]], 2)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for pts, k in test_cases:
        res = solve_optimal(pts, k)
        assert all((p in pts for p in res)) and len(res) == k
    print("All tests passed successfully!")
