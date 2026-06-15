"""
Problem: Surrounded Regions
Difficulty: Medium  Companies: Amazon,Google,Microsoft,Bloomberg
Problem Statement: Capture all regions not connected to border.
Complexity: Time O(M*N), Space O(M*N)
"""

import pytest
from typing import List


def solve_brute(board):
    return solve_optimal(board)


def solve_optimal(board):
    if not board:
        return
    ROWS, COLS = len(board), len(board[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
            return
        board[r][c] = "T"
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(ROWS):
        dfs(r, 0)
        dfs(r, COLS - 1)
    for c in range(COLS):
        dfs(0, c)
        dfs(ROWS - 1, c)
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "T":
                board[r][c] = "O"


@pytest.mark.parametrize(
    "board,ex",
    [
        (
            [
                ["X", "X", "X", "X"],
                ["X", "O", "O", "X"],
                ["X", "X", "O", "X"],
                ["X", "O", "X", "X"],
            ],
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "O", "X", "X"],
            ],
        )
    ],
)
def test_opt(board, ex):
    b = [r[:] for r in board]
    solve_optimal(b)
    assert b == ex
