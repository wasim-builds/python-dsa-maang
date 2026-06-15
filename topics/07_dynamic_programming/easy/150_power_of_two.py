"""
Problem: Power of Two
Difficulty: Easy  Companies: Amazon,Microsoft,Apple
Problem Statement: Return true if n is a power of two.
Complexity: Time O(1), Space O(1)
"""

import pytest


def solve_brute(n):
    return n > 0 and (n & (n - 1)) == 0


def solve_optimal(n):
    return n > 0 and not (n & (n - 1))


@pytest.mark.parametrize("n,ex", [(1, True), (16, True), (3, False), (0, False)])
def test_opt(n, ex):
    assert solve_optimal(n) == ex
