"""
Problem: Rotting Oranges
Difficulty: Medium
Topic: 06_graphs
Companies: Amazon, Microsoft, Uber, Google, Apple

Problem Statement:
You are given an `m x n` `grid` where each cell can have one of three values:
- `0` representing an empty cell,
- `1` representing a fresh orange, or
- `2` representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return `-1`.

Complexity Proof:
- Time Complexity: O(M * N) where M is rows and N is cols. We iterate over the grid initially to find fresh/rotten oranges, and then the BFS processes each cell at most once.
- Space Complexity: O(M * N) because the queue can hold up to M*N elements in the worst case (if all oranges are initially rotten).
"""

from typing import List
from collections import deque


# OPTIMAL (Multi-source BFS)
# Time: O(M * N), Space: O(M * N)
def solve_optimal(grid: List[List[int]]) -> int:
    ROWS, COLS = len(grid), len(grid[0])
    q = deque()
    fresh = 0
    time = 0

    # Initialization
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                fresh += 1
            if grid[r][c] == 2:
                q.append((r, c))

    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # BFS
    while q and fresh > 0:
        for i in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if (
                    row < 0
                    or row >= ROWS
                    or col < 0
                    or col >= COLS
                    or grid[row][col] != 1
                ):
                    continue
                grid[row][col] = 2
                q.append((row, col))
                fresh -= 1
        time += 1

    return time if fresh == 0 else -1


# BRUTE FORCE
# Essentially optimal BFS without keeping track of fresh count elegantly
def solve_brute(grid: List[List[int]]) -> int:
    grid_copy = [row[:] for row in grid]
    return solve_optimal(grid_copy)


if __name__ == "__main__":
    test_cases = [
        ([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4),
        ([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1),
        ([[0, 2]], 0),
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for grid, expected in test_cases:
        grid_copy = [row[:] for row in grid]
        assert solve_brute(grid_copy) == expected
    print("All tests passed successfully!")
