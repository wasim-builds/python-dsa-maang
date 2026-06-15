"""
Problem: K Closest Points to Origin
Difficulty: Easy  Companies: Amazon,Google,Meta,Facebook
Problem Statement: Return k closest points to origin.
Complexity: Time O(N log k), Space O(k)
"""

import pytest, heapq
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


@pytest.mark.parametrize(
    "pts,k", [([[1, 3], [-2, 2]], 1), ([[3, 3], [5, -1], [-2, 4]], 2)]
)
def test_opt(pts, k):
    res = solve_optimal(pts, k)
    assert all(p in pts for p in res) and len(res) == k
