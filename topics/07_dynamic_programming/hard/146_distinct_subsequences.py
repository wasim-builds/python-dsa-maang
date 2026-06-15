"""
Problem: Distinct Subsequences
Difficulty: Hard  Companies: Google,Snap,Amazon
Problem Statement: Count number of distinct subsequences of s which equals t.
Complexity: Time O(M*N), Space O(N)
"""

import pytest


def solve_brute(s, t):
    return solve_optimal(s, t)


def solve_optimal(s, t):
    m, n = len(s), len(t)
    dp = [0] * (n + 1)
    dp[0] = 1
    for c in s:
        for j in range(n, 0, -1):
            if c == t[j - 1]:
                dp[j] += dp[j - 1]
    return dp[n]


@pytest.mark.parametrize("s,t,ex", [("rabbbit", "rabbit", 3), ("babgbag", "bag", 5)])
def test_opt(s, t, ex):
    assert solve_optimal(s, t) == ex
