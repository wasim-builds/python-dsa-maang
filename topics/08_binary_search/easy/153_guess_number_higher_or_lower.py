"""
Problem: Guess Number Higher or Lower
Difficulty: Easy  Companies: Google,Amazon
Problem Statement: Binary search based guessing game.
Complexity: Time O(log N), Space O(1)
"""

import pytest


def guess(n, pick):
    return 0 if n == pick else (-1 if n > pick else 1)


def solve_optimal(n, pick):
    l, r = 1, n
    while l <= r:
        mid = (l + r) // 2
        g = guess(mid, pick)
        if g == 0:
            return mid
        elif g < 0:
            r = mid - 1
        else:
            l = mid + 1


def solve_brute(n, pick):
    return solve_optimal(n, pick)


@pytest.mark.parametrize("n,pick,ex", [(10, 6, 6), (1, 1, 1), (2, 2, 2)])
def test_opt(n, pick, ex):
    assert solve_optimal(n, pick) == ex
