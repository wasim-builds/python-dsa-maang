"""
Problem: First Bad Version
Difficulty: Easy  Companies: Facebook,Amazon,Google,Microsoft
Problem Statement: Find first bad version minimizing API calls.
Complexity: Time O(log N), Space O(1)
"""

import pytest


def is_bad(v, bad):
    return v >= bad


def solve_optimal(n, bad):
    l, r = 1, n
    while l < r:
        mid = (l + r) // 2
        if is_bad(mid, bad):
            r = mid
        else:
            l = mid + 1
    return l


def solve_brute(n, bad):
    for i in range(1, n + 1):
        if is_bad(i, bad):
            return i


@pytest.mark.parametrize("n,b,ex", [(5, 4, 4), (1, 1, 1)])
def test_opt(n, b, ex):
    assert solve_optimal(n, b) == ex
