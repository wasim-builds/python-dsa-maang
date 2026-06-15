"""
Problem: Minimum Flips to Make a OR b Equal to c
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Return min number of flips required to make a OR b == c.
Complexity: Time O(log N), Space O(1)
"""

import pytest


def solve_brute(a, b, c):
    return solve_optimal(a, b, c)


def solve_optimal(a, b, c):
    count = 0
    while a or b or c:
        ab = a & 1
        bb = b & 1
        cb = c & 1
        if cb == 0:
            count += ab + bb
        elif ab == 0 and bb == 0:
            count += 1
        a >>= 1
        b >>= 1
        c >>= 1
    return count


@pytest.mark.parametrize("a,b,c,ex", [(2, 6, 5, 3), (4, 2, 7, 1), (1, 2, 3, 0)])
def test_opt(a, b, c, ex):
    assert solve_optimal(a, b, c) == ex
