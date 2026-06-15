"""
Problem: Find K Closest Elements
Difficulty: Medium  Companies: LinkedIn,Google,Facebook,Amazon
Problem Statement: Given sorted array, find k closest elements to x. Return sorted.
Complexity: Time O(log N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(arr, k, x):
    arr.sort(key=lambda n: abs(n - x))
    return sorted(arr[:k])


def solve_optimal(arr, k, x):
    l, r = 0, len(arr) - k
    while l < r:
        mid = (l + r) // 2
        if x - arr[mid] > arr[mid + k] - x:
            l = mid + 1
        else:
            r = mid
    return arr[l : l + k]


@pytest.mark.parametrize(
    "arr,k,x,ex",
    [([1, 2, 3, 4, 5], 4, 3, [1, 2, 3, 4]), ([1, 2, 3, 4, 5], 4, -1, [1, 2, 3, 4])],
)
def test_opt(arr, k, x, ex):
    assert solve_optimal(arr, k, x) == ex
