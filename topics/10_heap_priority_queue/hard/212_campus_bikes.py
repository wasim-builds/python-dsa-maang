"""
Problem: The K Weakest Rows in a Matrix
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Return k weakest rows (by soldier count, then row index).
Complexity: Time O(M * N), Space O(M)
"""

import pytest, heapq
from typing import List


def solve_brute(mat, k):
    rows = sorted(range(len(mat)), key=lambda i: (sum(mat[i]), i))
    return rows[:k]


def solve_optimal(mat, k):
    heap = []
    for i, row in enumerate(mat):
        heapq.heappush(heap, (sum(row), i))
    return [heapq.heappop(heap)[1] for _ in range(k)]


@pytest.mark.parametrize(
    "m,k,ex",
    [
        (
            [
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1],
            ],
            3,
            [2, 0, 3],
        )
    ],
)
def test_opt(m, k, ex):
    assert solve_optimal(m, k) == ex
