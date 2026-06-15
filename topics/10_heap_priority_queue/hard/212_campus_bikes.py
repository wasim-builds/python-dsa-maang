"""
Problem: The K Weakest Rows in a Matrix
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Return k weakest rows (by soldier count, then row index).
Complexity: Time O(M * N), Space O(M)
"""

import heapq
from typing import List


def solve_brute(mat, k):
    rows = sorted(range(len(mat)), key=lambda i: (sum(mat[i]), i))
    return rows[:k]


def solve_optimal(mat, k):
    heap = []
    for i, row in enumerate(mat):
        heapq.heappush(heap, (sum(row), i))
    return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == "__main__":
    test_cases = [
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
    ]
    if (
        isinstance(test_cases, tuple)
        and len(test_cases) > 0
        and not isinstance(test_cases[0], (tuple, list))
    ):
        test_cases = [test_cases]
    elif not isinstance(test_cases, (list, tuple)):
        test_cases = [test_cases]

    for m, k, ex in test_cases:
        assert solve_optimal(m, k) == ex
    print("All tests passed successfully!")
