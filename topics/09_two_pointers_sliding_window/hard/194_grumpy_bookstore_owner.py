"""
Problem: Grumpy Bookstore Owner
Difficulty: Hard  Companies: Amazon,Google
Problem Statement: Find max customers satisfied using 'grumpy' suppression window of size minutes.
Complexity: Time O(N), Space O(1)
"""

import pytest
from typing import List


def solve_brute(customers, grumpy, minutes):
    always = sum(c for c, g in zip(customers, grumpy) if g == 0)
    best = 0
    for i in range(len(customers) - minutes + 1):
        extra = sum(
            c
            for c, g in zip(customers[i : i + minutes], grumpy[i : i + minutes])
            if g == 1
        )
        best = max(best, extra)
    return always + best


def solve_optimal(customers, grumpy, minutes):
    always = sum(c for c, g in zip(customers, grumpy) if g == 0)
    window = sum(c * g for c, g in zip(customers[:minutes], grumpy[:minutes]))
    best = window
    for i in range(minutes, len(customers)):
        window += (
            customers[i] * grumpy[i] - customers[i - minutes] * grumpy[i - minutes]
        )
        best = max(best, window)
    return always + best


@pytest.mark.parametrize(
    "c,g,m,ex", [([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3, 16)]
)
def test_opt(c, g, m, ex):
    assert solve_optimal(c, g, m) == ex
