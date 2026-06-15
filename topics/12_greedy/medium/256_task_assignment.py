"""
Problem: Score After Flipping Matrix
Difficulty: Medium  Companies: Google,Amazon
Problem Statement: Toggle rows/cols to maximize score of binary matrix.
Complexity: Time O(M*N), Space O(1)
"""

from typing import List


def solve_brute(grid):
    return solve_optimal(grid)


def solve_optimal(grid):
    m, n = len(grid), len(grid[0])
    for row in grid:
        if not row[0]:
            for j in range(n):
                row[j] ^= 1
    for j in range(1, n):
        ones = sum(grid[i][j] for i in range(m))
        if ones < m - ones:
            for i in range(m):
                grid[i][j] ^= 1
    return sum(int("".join(map(str, row)), 2) for row in grid)


if __name__ == "__main__":
    test_cases = [([[0, 0, 1, 1], [1, 0, 1, 0], [1, 1, 0, 0]], 39)]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for g, ex in test_cases:
        assert solve_optimal([r[:] for r in g]) == ex
    print("All tests passed successfully!")
