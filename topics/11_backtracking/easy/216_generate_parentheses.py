"""
Problem: Generate Parentheses
Difficulty: Easy  Companies: Amazon,Google,Meta,Bloomberg,Microsoft
Problem Statement: Generate all combinations of n pairs of well-formed parentheses.
Complexity: Time O(4^N / sqrt(N)) Catalan, Space O(N)
"""

import pytest
from typing import List


def solve_brute(n):
    return solve_optimal(n)


def solve_optimal(n):
    res = []

    def bt(s, open, close):
        if len(s) == 2 * n:
            res.append(s)
            return
        if open < n:
            bt(s + "(", open + 1, close)
        if close < open:
            bt(s + ")", open, close + 1)

    bt("", 0, 0)
    return res


@pytest.mark.parametrize(
    "n,ex", [(3, ["((()))", "(()())", "(())()", "()(())", "()()()"]), (1, ["()"])]
)
def test_opt(n, ex):
    assert sorted(solve_optimal(n)) == sorted(ex)
