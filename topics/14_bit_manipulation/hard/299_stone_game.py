"""
Problem: Stone Game II
Difficulty: Hard  Companies: Google,Amazon
Problem Statement: Alex and Lee take turns. Find max stones Alex can get.
Complexity: Time O(N^2), Space O(N^2)
"""

import pytest
from typing import List


def solve_brute(piles):
    return solve_optimal(piles)


def solve_optimal(piles):
    n = len(piles)
    suffix = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        suffix[i] = suffix[i + 1] + piles[i]
    from functools import lru_cache

    @lru_cache(None)
    def dp(i, m):
        if i + 2 * m >= n:
            return suffix[i]
        best = 0
        for x in range(1, 2 * m + 1):
            best = max(best, suffix[i] - dp(i + x, max(m, x)))
        return best

    return dp(0, 1)


@pytest.mark.parametrize("p,ex", [([2, 7, 9, 4, 4], 10), ([1, 2, 3, 4, 5, 100], 104)])
def test_opt(p, ex):
    assert solve_optimal(p) == ex
