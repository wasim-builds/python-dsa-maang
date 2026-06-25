"""
Problem: Valid Sudoku
Difficulty: Medium
Topic: 01_arrays
Companies: Amazon, Apple, Microsoft, Uber, Google

Problem Statement:
Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.
Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable.

Complexity Proof:
- Time Complexity: O(1) or O(9^2) because the board size is fixed at 9x9. We iterate through 81 cells once.
- Space Complexity: O(1) or O(9^2) because the hash sets will store at most 81 elements across rows, cols, and squares.
"""

from typing import List
from collections import defaultdict


# OPTIMAL
# Time: O(9^2), Space: O(9^2)
def solve_optimal(board: List[List[str]]) -> bool:
    cols = defaultdict(set)
    rows = defaultdict(set)
    squares = defaultdict(set)  # key = (r//3, c//3)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (
                board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[(r // 3, c // 3)]
            ):
                return False

            cols[c].add(board[r][c])
            rows[r].add(board[r][c])
            squares[(r // 3, c // 3)].add(board[r][c])

    return True


# BRUTE FORCE
# Brute force is effectively the same as optimal, since we must check every cell.
def solve_brute(board: List[List[str]]) -> bool:
    return solve_optimal(board)


if __name__ == "__main__":
    test_cases = [
        (
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            True,
        )
    ]

    for board, expected in test_cases:
        assert solve_brute(board) == expected
    print("All tests passed successfully!")
