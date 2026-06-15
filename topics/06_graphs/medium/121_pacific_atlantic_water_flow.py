"""
Problem: Pacific Atlantic Water Flow
Difficulty: Medium
Topic: 06_graphs
Companies: Amazon, Google, Meta, Microsoft, Apple

Problem Statement:
There is an `m x n` rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.
The island is partitioned into a grid of square cells. You are given an `m x n` integer matrix `heights` where `heights[r][c]` represents the height above sea level of the cell at coordinate `(r, c)`.
The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.
Return a 2D list of grid coordinates `result` where `result[i] = [ri, ci]` denotes that rain water can flow from cell `(ri, ci)` to both the Pacific and Atlantic oceans.

Complexity Proof:
- Time Complexity: O(M * N) where M is the number of rows and N is the number of columns. We run DFS from the ocean borders inward. Each cell is visited at most once per ocean.
- Space Complexity: O(M * N) to store the `pac` and `atl` hash sets and for the DFS recursion stack.
"""

import pytest
from typing import List


# OPTIMAL (Multi-source DFS from Oceans)
# Time: O(M * N), Space: O(M * N)
def solve_optimal(heights: List[List[int]]) -> List[List[int]]:
    if not heights:
        return []

    ROWS, COLS = len(heights), len(heights[0])
    pac, atl = set(), set()

    def dfs(r, c, visit, prevHeight):
        if (
            (r, c) in visit
            or r < 0
            or c < 0
            or r >= ROWS
            or c >= COLS
            or heights[r][c] < prevHeight
        ):
            return

        visit.add((r, c))
        dfs(r + 1, c, visit, heights[r][c])
        dfs(r - 1, c, visit, heights[r][c])
        dfs(r, c + 1, visit, heights[r][c])
        dfs(r, c - 1, visit, heights[r][c])

    for c in range(COLS):
        dfs(0, c, pac, heights[0][c])
        dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

    for r in range(ROWS):
        dfs(r, 0, pac, heights[r][0])
        dfs(r, COLS - 1, atl, heights[r][COLS - 1])

    res = []
    for r in range(ROWS):
        for c in range(COLS):
            if (r, c) in pac and (r, c) in atl:
                res.append([r, c])

    return res


# BRUTE FORCE
# Run DFS from EVERY cell to see if it reaches both oceans.
# Time: O((M * N)^2), Space: O(M * N)
def solve_brute(heights: List[List[int]]) -> List[List[int]]:
    if not heights:
        return []

    ROWS, COLS = len(heights), len(heights[0])
    res = []

    def dfs(r, c, visit):
        pac_reach, atl_reach = False, False
        if r == 0 or c == 0:
            pac_reach = True
        if r == ROWS - 1 or c == COLS - 1:
            atl_reach = True

        visit.add((r, c))

        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                0 <= nr < ROWS
                and 0 <= nc < COLS
                and (nr, nc) not in visit
                and heights[nr][nc] <= heights[r][c]
            ):
                p, a = dfs(nr, nc, visit)
                pac_reach = pac_reach or p
                atl_reach = atl_reach or a

        return pac_reach, atl_reach

    for r in range(ROWS):
        for c in range(COLS):
            p, a = dfs(r, c, set())
            if p and a:
                res.append([r, c])

    return res


@pytest.mark.parametrize(
    "heights, expected",
    [
        (
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
        ),
        ([[1]], [[0, 0]]),
    ],
)
def test_solve_optimal(heights, expected):
    assert solve_optimal(heights) == expected


@pytest.mark.parametrize(
    "heights, expected",
    [
        (
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
        ),
        ([[1]], [[0, 0]]),
    ],
)
def test_solve_brute(heights, expected):
    assert solve_brute(heights) == expected
