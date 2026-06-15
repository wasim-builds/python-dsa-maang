"""
Problem: Combinations (k of n)
Difficulty: Hard  Companies: Amazon,Google,Microsoft
Problem Statement: Return all combinations of k numbers chosen from 1..n.
Complexity: Time O(C(n,k) * k), Space O(k)
"""

import pytest
from typing import List


def solve_brute(n, k):
    return solve_optimal(n, k)


def solve_optimal(n, k):
    res = []

    def bt(start, comb):
        if len(comb) == k:
            res.append(comb[:])
            return
        for i in range(start, n + 1):
            comb.append(i)
            bt(i + 1, comb)
            comb.pop()

    bt(1, [])
    return res


@pytest.mark.parametrize(
    "n,k,ex", [(4, 2, [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]), (1, 1, [[1]])]
)
def test_opt(n, k, ex):
    assert sorted(solve_optimal(n, k)) == sorted(ex)
