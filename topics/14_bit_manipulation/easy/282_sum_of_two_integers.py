"""
Problem: Sum of Two Integers (No + operator)
Difficulty: Easy  Companies: Amazon,Facebook,Microsoft
Problem Statement: Return sum of two integers without using + or - operators.
Complexity: Time O(1), Space O(1)
"""

import pytest


def solve_brute(a, b):
    return a + b


def solve_optimal(a, b):
    mask = 0xFFFFFFFF
    while b & mask:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    return (a & mask) if b > 0 else a


@pytest.mark.parametrize("a,b,ex", [(1, 2, 3), (-2, 3, 1)])
def test_opt(a, b, ex):
    assert solve_optimal(a, b) == ex
