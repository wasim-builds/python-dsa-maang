"""
Problem: Pascal's Triangle
Difficulty: Easy  Companies: Amazon,Microsoft,Apple
Problem Statement: Generate first numRows of Pascal's Triangle.
Complexity: Time O(N^2), Space O(N^2)
"""

import pytest
from typing import List


def solve_brute(n):
    res = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(res[i - 1][j - 1] + res[i - 1][j])
        row.append(1)
        res.append(row)
    return res


def solve_optimal(n):
    return solve_brute(n)


@pytest.mark.parametrize(
    "n,ex", [(5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]), (1, [[1]])]
)
def test_opt(n, ex):
    assert solve_optimal(n) == ex
