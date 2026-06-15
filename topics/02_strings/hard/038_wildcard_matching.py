"""
Problem: Wildcard Matching
Difficulty: Hard
Topic: 02_strings  Companies: Facebook,Amazon,Google,Microsoft
Problem Statement: Match string s to pattern p with '?' and '*'.
Complexity: Time O(M*N), Space O(M*N)
"""

import pytest


def solve_brute(s, p):
    import re

    p2 = re.escape(p).replace(r"\?", ".").replace(r"\*", ".*")
    return bool(re.fullmatch(p2, s))


def solve_optimal(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(1, n + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 1]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            elif p[j - 1] == "?" or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[m][n]


@pytest.mark.parametrize(
    "s,p,ex",
    [
        ("aa", "a", False),
        ("aa", "*", True),
        ("cb", "?a", False),
        ("adceb", "*a*b", True),
    ],
)
def test_opt(s, p, ex):
    assert solve_optimal(s, p) == ex
