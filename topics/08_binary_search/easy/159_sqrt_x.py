"""
Problem: Sqrt(x)
Difficulty: Easy  Companies: Amazon,Google,Microsoft,Bloomberg
Problem Statement: Compute integer square root (truncated) without using sqrt function.
Complexity: Time O(log N), Space O(1)
"""

import pytest


def solve_brute(x):
    return int(x**0.5)


def solve_optimal(x):
    if x < 2:
        return x
    l, r = 1, x // 2
    while l <= r:
        mid = (l + r) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            l = mid + 1
        else:
            r = mid - 1
    return r


@pytest.mark.parametrize("x,ex", [(4, 2), (8, 2), (0, 0), (1, 1)])
def test_opt(x, ex):
    assert solve_optimal(x) == ex
