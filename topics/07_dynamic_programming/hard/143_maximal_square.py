"""
Problem: Maximal Square
Difficulty: Hard  Companies: Amazon,Facebook,Google,Uber
Problem Statement: Find largest square containing only 1s in binary matrix. Return its area.
Complexity: Time O(M*N), Space O(N)
"""

from typing import List


def solve_brute(matrix):
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "1":
                side = 1
                while True:
                    ni, nj = i + side, j + side
                    if ni > len(matrix) or nj > len(matrix[0]):
                        break
                    if all(
                        matrix[r][c] == "1" for r in range(i, ni) for c in range(j, nj)
                    ):
                        side += 1
                    else:
                        break
                res = max(res, (side) ** 2)
    return res


def solve_optimal(matrix):
    if not matrix:
        return 0
    m, n = len(matrix), len(matrix[0])
    prev = [0] * n
    res = 0
    for i in range(m):
        curr = [0] * n
        for j in range(n):
            if matrix[i][j] == "1":
                curr[j] = (
                    min(
                        prev[j],
                        curr[j - 1] if j > 0 else 0,
                        prev[j - 1] if j > 0 else 0,
                    )
                    + 1
                )
                res = max(res, curr[j])
        prev = curr
    return res * res


if __name__ == "__main__":
    test_cases = [
        (
            [
                ["1", "0", "1", "0", "0"],
                ["1", "0", "1", "1", "1"],
                ["1", "1", "1", "1", "1"],
                ["1", "0", "0", "1", "0"],
            ],
            4,
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

    for m, ex in test_cases:
        assert solve_optimal(m) == ex
    print("All tests passed successfully!")
