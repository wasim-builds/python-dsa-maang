"""
Problem: Swim in Rising Water
Difficulty: Hard  Companies: Google,Amazon
Problem Statement: Find minimum time T such that you can swim from [0][0] to [N-1][N-1].
Complexity: Time O(N^2 log N), Space O(N^2)
"""

from typing import List
import heapq


def solve_brute(grid):
    return solve_optimal(grid)


def solve_optimal(grid):
    n = len(grid)
    visited = set()
    heap = [(grid[0][0], 0, 0)]
    while heap:
        t, r, c = heapq.heappop(heap)
        if r == n - 1 and c == n - 1:
            return t
        if (r, c) in visited:
            continue
        visited.add((r, c))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                heapq.heappush(heap, (max(t, grid[nr][nc]), nr, nc))


if __name__ == "__main__":
    test_cases = [
        ([[0, 2], [1, 3]], 3),
        (
            [
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6],
            ],
            16,
        ),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for g, ex in test_cases:
        assert solve_optimal(g) == ex
    print("All tests passed successfully!")
