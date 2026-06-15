"""
Problem: Number of Steps to Reduce a Number to Zero
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Return number of steps to reduce n to zero (even: div 2, odd: subtract 1).
Complexity: Time O(log N), Space O(1)
"""

import pytest


def solve_brute(n):
    return solve_optimal(n)


def solve_optimal(n):
    steps = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
        steps += 1
    return steps


@pytest.mark.parametrize("n,ex", [(14, 6), (8, 4), (123, 12)])
def test_opt(n, ex):
    assert solve_optimal(n) == ex
