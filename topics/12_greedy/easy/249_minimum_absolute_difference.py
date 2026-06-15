"""
Problem: Minimum Absolute Difference
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Find all pairs with minimum absolute difference. Return sorted.
Complexity: Time O(N log N), Space O(N)
"""

import pytest
from typing import List


def solve_brute(arr):
    return solve_optimal(arr)


def solve_optimal(arr):
    arr.sort()
    mn = min(arr[i + 1] - arr[i] for i in range(len(arr) - 1))
    return [
        [arr[i], arr[i + 1]] for i in range(len(arr) - 1) if arr[i + 1] - arr[i] == mn
    ]


@pytest.mark.parametrize(
    "arr,ex", [([4, 2, 1, 3], [[1, 2], [2, 3], [3, 4]]), ([1, 3, 6, 10, 15], [[1, 3]])]
)
def test_opt(arr, ex):
    assert solve_optimal(arr) == ex
