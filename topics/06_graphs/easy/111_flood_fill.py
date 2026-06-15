"""
Problem: Flood Fill
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Given image, sr, sc, color. Flood fill starting from (sr,sc).
Complexity: Time O(N), Space O(N)
"""

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


if __name__ == "__main__":
    test_cases = [
        ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]])
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for img, sr, sc, col, ex in test_cases:
        assert solve_optimal([r[:] for r in img], sr, sc, col) == ex
    print("All tests passed successfully!")
