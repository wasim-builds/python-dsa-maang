"""
Problem: Word Search
Difficulty: Medium
Topic: 11_backtracking
Companies: Amazon, Microsoft, Bloomberg, Meta, Apple

Problem Statement:
Given an `m x n` grid of characters `board` and a string `word`, return `true` if `word` exists in the grid.
The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Complexity Proof:
- Time Complexity: O(M * N * 3^L) where M is rows, N is cols, and L is the length of the word. From each cell, we explore up to 3 directions (avoiding the one we came from).
- Space Complexity: O(L) for the DFS recursion stack. The visited set can also be avoided by modifying the board in place, keeping space at O(L).
"""

from typing import List


# OPTIMAL (Backtracking DFS)
# Time: O(N * M * 3^L), Space: O(L)
def solve_optimal(board: List[List[str]], word: str) -> bool:
    ROWS, COLS = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True

        if (
            r < 0
            or c < 0
            or r >= ROWS
            or c >= COLS
            or board[r][c] != word[i]
            or board[r][c] == "#"
        ):
            return False

        # Mark visited
        temp = board[r][c]
        board[r][c] = "#"

        # Explore neighbors
        res = (
            dfs(r + 1, c, i + 1)
            or dfs(r - 1, c, i + 1)
            or dfs(r, c + 1, i + 1)
            or dfs(r, c - 1, i + 1)
        )

        # Backtrack (Unmark visited)
        board[r][c] = temp
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if dfs(r, c, 0):
                return True

    return False


# Brute force is essentially the same algorithm since we must try all paths.
def solve_brute(board: List[List[str]], word: str) -> bool:
    return solve_optimal(board, word)


if __name__ == "__main__":
    test_cases = [
        (
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
            "ABCCED",
            True,
        )
    ]

    for board, word, expected in test_cases:
        test_board = [row[:] for row in board]
        assert solve_brute(test_board, word) == expected
    print("All tests passed successfully!")
