"""
Problem: Number of 1 Bits (Hamming Weight)
Difficulty: Easy  Companies: Amazon,Microsoft,Apple
Problem Statement: Return number of 1 bits (Hamming weight) of integer n.
Complexity: Time O(1), Space O(1)
"""

import pytest


def solve_brute(n):
    return bin(n).count("1")


def solve_optimal(n):
    count = 0
    while n:
        n &= n - 1
        count += 1
    return count


@pytest.mark.parametrize("n,ex", [(11, 3), (128, 1), (4294967293, 31)])
def test_opt(n, ex):
    assert solve_optimal(n) == ex
