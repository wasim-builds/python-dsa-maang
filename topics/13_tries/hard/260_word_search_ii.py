"""
Problem: Word Search II
Difficulty: Hard
Topic: 13_tries
Companies: Microsoft, Amazon, Google, Meta, Apple

Problem Statement:
Given an `m x n` `board` of characters and a list of strings `words`, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Complexity Proof:
- Time Complexity: O(M * N * 3^L) where M and N are the dimensions of the board and L is the maximum length of a word. By building a Trie, we prune the DFS tree aggressively if a prefix doesn't exist, vastly outperforming standard DFS for multiple words.
- Space Complexity: O(W) where W is the total number of characters in all words to build the Trie, plus O(L) for the DFS recursion stack.
"""

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = word


# OPTIMAL (Trie + Backtracking DFS)
# Time: O(M * N * 3^L), Space: O(W + L)
def solve_optimal(board: List[List[str]], words: List[str]) -> List[str]:
    trie = Trie()
    for w in words:
        trie.insert(w)

    ROWS, COLS = len(board), len(board[0])
    res = []

    def dfs(r, c, node):
        if (
            r < 0
            or c < 0
            or r >= ROWS
            or c >= COLS
            or board[r][c] not in node.children
            or board[r][c] == "#"
        ):
            return

        temp = board[r][c]
        curr_node = node.children[temp]

        # Word found
        if curr_node.word:
            res.append(curr_node.word)
            curr_node.word = None  # Prevent duplicates

        board[r][c] = "#"  # Mark visited

        dfs(r + 1, c, curr_node)
        dfs(r - 1, c, curr_node)
        dfs(r, c + 1, curr_node)
        dfs(r, c - 1, curr_node)

        board[r][c] = temp  # Unmark

        # Optimization: prune leaf nodes to speed up further searches
        if not curr_node.children:
            del node.children[temp]

    for r in range(ROWS):
        for c in range(COLS):
            dfs(r, c, trie.root)

    return res


# BRUTE FORCE (Standard DFS per word)
# Time: O(K * M * N * 3^L) where K is number of words
def solve_brute(board: List[List[str]], words: List[str]) -> List[str]:
    ROWS, COLS = len(board), len(board[0])
    res = []

    def dfs(r, c, word, i):
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

        temp = board[r][c]
        board[r][c] = "#"

        found = (
            dfs(r + 1, c, word, i + 1)
            or dfs(r - 1, c, word, i + 1)
            or dfs(r, c + 1, word, i + 1)
            or dfs(r, c - 1, word, i + 1)
        )

        board[r][c] = temp
        return found

    for w in words:
        found = False
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, w, 0):
                    res.append(w)
                    found = True
                    break
            if found:
                break

    return res


if __name__ == "__main__":
    test_cases = [
        (
            [
                ["o", "a", "a", "n"],
                ["e", "t", "a", "e"],
                ["i", "h", "k", "r"],
                ["i", "f", "l", "v"],
            ],
            ["oath", "pea", "eat", "rain"],
            ["eat", "oath"],
        )
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for board, words, expected in test_cases:
        board_copy = [row[:] for row in board]
        assert sorted(solve_brute(board_copy, words)) == sorted(expected)
    print("All tests passed successfully!")
