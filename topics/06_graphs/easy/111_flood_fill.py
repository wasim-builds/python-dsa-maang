"""
Problem: Flood Fill
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Given image, sr, sc, color. Flood fill starting from (sr,sc).
Complexity: Time O(N), Space O(N)
"""

import pytest
from typing import List


def solve_brute(image, sr, sc, color):
    orig = image[sr][sc]
    if orig == color:
        return image

    def dfs(r, c):
        if (
            r < 0
            or c < 0
            or r >= len(image)
            or c >= len(image[0])
            or image[r][c] != orig
        ):
            return
        image[r][c] = color
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    dfs(sr, sc)
    return image


def solve_optimal(image, sr, sc, color):
    return solve_brute(image, sr, sc, color)


@pytest.mark.parametrize(
    "img,sr,sc,col,ex",
    [([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]])],
)
def test_opt(img, sr, sc, col, ex):
    assert solve_optimal([r[:] for r in img], sr, sc, col) == ex
