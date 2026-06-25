"""
Problem: Min Cost to Connect All Points
Difficulty: Hard  Companies: Amazon,Google,Microsoft
Problem Statement: Connect all points with minimum cost (Euclidean distance). Return min cost.
Complexity: Time O(N^2 log N) Prim's, Space O(N)
"""

from typing import List
import heapq


def solve_brute(points):
    return solve_optimal(points)


def solve_optimal(points):
    n = len(points)
    visited = set()
    heap = [(0, 0)]
    total = 0
    while len(visited) < n:
        cost, i = heapq.heappop(heap)
        if i in visited:
            continue
        visited.add(i)
        total += cost
        for j in range(n):
            if j not in visited:
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(heap, (d, j))
    return total


if __name__ == "__main__":
    test_cases = [
        ([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]], 20),
        ([[3, 12], [-2, 5], [-4, 1]], 18),
    ]

    for pts, ex in test_cases:
        assert solve_optimal(pts) == ex
    print("All tests passed successfully!")
