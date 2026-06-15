"""
Problem: Fibonacci Number
Difficulty: Easy  Companies: Amazon,Microsoft,Apple
Problem Statement: Return the nth Fibonacci number.
Complexity: Time O(N), Space O(1)
"""

import pytest


def solve_brute(n):
    if n <= 1:
        return n
    return solve_brute(n - 1) + solve_brute(n - 2)


def solve_optimal(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


@pytest.mark.parametrize("n,ex", [(2, 1), (3, 2), (4, 3), (10, 55)])
def test_opt(n, ex):
    assert solve_optimal(n) == ex


@pytest.mark.parametrize("n,ex", [(5, 5)])
def test_brute(n, ex):
    assert solve_brute(n) == ex
