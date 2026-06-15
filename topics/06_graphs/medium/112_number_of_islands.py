"""
Problem: Number of Islands
Difficulty: Medium
Topic: 06_graphs
Companies: Amazon, Microsoft, Bloomberg, Google, LinkedIn

Problem Statement:
Given an `m x n` 2D binary grid `grid` which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Complexity Proof:
- Time Complexity: O(M * N) where M is the number of rows and N is the number of columns. We visit every cell in the grid exactly once.
- Space Complexity: O(M * N) in the worst case (if the entire grid is land) for the recursive call stack in DFS, or for the queue in BFS.
"""

from typing import List
from collections import deque


# BRUTE FORCE / ALTERNATIVE (BFS)
# Time: O(M * N), Space: O(min(M, N)) for the queue
def solve_brute(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def bfs(r, c):
        q = deque()
        q.append((r, c))
        grid_copy[r][c] = "0"

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q:
            row, col = q.popleft()
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid_copy[nr][nc] == "1":
                    grid_copy[nr][nc] = "0"  # mark visited immediately
                    q.append((nr, nc))

    # We need to make a deep copy to not mutate the original during tests
    grid_copy = [row[:] for row in grid]

    for r in range(rows):
        for c in range(cols):
            if grid_copy[r][c] == "1":
                bfs(r, c)
                islands += 1

    return islands


# OPTIMAL (DFS)
# Time: O(M * N), Space: O(M * N)
def solve_optimal(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid_copy[r][c] == "0":
            return

        grid_copy[r][c] = "0"  # Mark visited

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    grid_copy = [row[:] for row in grid]

    for r in range(rows):
        for c in range(cols):
            if grid_copy[r][c] == "1":
                dfs(r, c)
                islands += 1

    return islands


if __name__ == "__main__":
    test_cases = [
        (
            [
                ["1", "1", "1", "1", "0"],
                ["1", "1", "0", "1", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "0", "0", "0"],
            ],
            1,
        ),
        (
            [
                ["1", "1", "0", "0", "0"],
                ["1", "1", "0", "0", "0"],
                ["0", "0", "1", "0", "0"],
                ["0", "0", "0", "1", "1"],
            ],
            3,
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

    for grid, expected in test_cases:
        assert solve_brute(grid) == expected
    print("All tests passed successfully!")
