"""
Problem: Sudoku Solver
Difficulty: Medium  Companies: Amazon,Google,Microsoft,Uber
Problem Statement: Solve sudoku puzzle by filling empty cells.
Complexity: Time O(9^M) where M is empty cells, Space O(M)
"""

import pytest
from typing import List


def solve_brute(board):
    return solve_optimal(board)


def solve_optimal(board):
    def is_valid(r, c, v):
        if v in board[r]:
            return False
        if any(board[i][c] == v for i in range(9)):
            return False
        br, bc = 3 * (r // 3), 3 * (c // 3)
        if any(board[br + i][bc + j] == v for i in range(3) for j in range(3)):
            return False
        return True

    def bt():
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    for v in "123456789":
                        if is_valid(r, c, v):
                            board[r][c] = v
                            if bt():
                                return True
                            board[r][c] = "."
                    return False
        return True

    bt()


def test_sudoku():
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    solve_optimal(board)
    assert board[0][2] == "4"
