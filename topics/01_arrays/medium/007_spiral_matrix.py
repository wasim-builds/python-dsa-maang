"""
Problem: Spiral Matrix
Difficulty: Medium
Topic: 01_arrays  Companies: Amazon,Microsoft,Apple,Bloomberg
Problem Statement: Given m x n matrix, return all elements in spiral order.
Complexity: Time O(M*N), Space O(1) excluding output
"""

from typing import List


def solve_brute(matrix):
    res = []
    while matrix:
        res += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                res.append(row.pop())
        if matrix:
            res += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                res.append(row.pop(0))
    return res


def solve_optimal(matrix):
    res = []
    l, r, t, b = 0, len(matrix[0]), 0, len(matrix)
    while l < r and t < b:
        for i in range(l, r):
            res.append(matrix[t][i])
        t += 1
        for i in range(t, b):
            res.append(matrix[i][r - 1])
        r -= 1
        if not (l < r and t < b):
            break
        for i in range(r - 1, l - 1, -1):
            res.append(matrix[b - 1][i])
        b -= 1
        for i in range(b - 1, t - 1, -1):
            res.append(matrix[i][l])
        l += 1
    return res


if __name__ == "__main__":
    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        (
            [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
    ]

    for m, ex in test_cases:
        assert solve_optimal(m) == ex
    print("All tests passed successfully!")
