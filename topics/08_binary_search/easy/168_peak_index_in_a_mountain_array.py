"""
Problem: Peak Index in a Mountain Array
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Find peak index in mountain array.
Complexity: Time O(log N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(arr):
    return arr.index(max(arr))


def solve_optimal(arr):
    l, r = 0, len(arr) - 1
    while l < r:
        mid = (l + r) // 2
        if arr[mid] > arr[mid + 1]:
            r = mid
        else:
            l = mid + 1
    return l


@pytest.mark.parametrize(
    "arr,ex", [([0, 1, 0], 1), ([0, 2, 1, 0], 1), ([0, 10, 5, 2], 1)]
)
def test_opt(arr, ex):
    assert solve_optimal(arr) == ex
