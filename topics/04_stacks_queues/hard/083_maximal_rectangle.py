"""
Problem: Maximal Rectangle
Difficulty: Hard  Companies: Amazon,Google,Microsoft,Meta
Problem Statement: Given binary matrix, find largest rectangle containing only 1s.
Complexity: Time O(M*N), Space O(N)
"""

import pytest
from typing import List


def solve_brute(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    res = 0
    heights = [0] * n
    for row in matrix:
        for j in range(n):
            heights[j] = heights[j] + 1 if row[j] == "1" else 0
        for i in range(n):
            mn = heights[i]
            for j in range(i, -1, -1):
                mn = min(mn, heights[j])
                res = max(res, mn * (i - j + 1))
    return res


def largest_rect(heights):
    stack = []
    maxA = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, ht = stack.pop()
            maxA = max(maxA, ht * (i - idx))
            start = idx
        stack.append((start, h))
    for i, h in stack:
        maxA = max(maxA, h * (len(heights) - i))
    return maxA


def solve_optimal(matrix):
    if not matrix:
        return 0
    n = len(matrix[0])
    heights = [0] * n
    res = 0
    for row in matrix:
        for j in range(n):
            heights[j] = heights[j] + 1 if row[j] == "1" else 0
        res = max(res, largest_rect(heights))
    return res


@pytest.mark.parametrize(
    "m,ex",
    [
        (
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
            6,
        )
    ],
)
def test_opt(m, ex):
    assert solve_optimal(m) == ex
