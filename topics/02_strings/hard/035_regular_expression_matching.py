"""
Problem: Regular Expression Matching
Difficulty: Hard
Topic: 02_strings  Companies: Google,Meta,Amazon,Microsoft
Problem Statement: Given string s and pattern p with '.' and '*', implement regular expression matching.
Complexity: Time O(M*N), Space O(M*N)
"""

import pytest


def solve_brute(s, p):
    import re

    return bool(re.fullmatch(p, s))


def solve_optimal(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for j in range(1, n + 1):
        if p[j - 1] == "*":
            dp[0][j] = dp[0][j - 2]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[i][j] = dp[i][j - 2] or (
                    dp[i - 1][j] and (p[j - 2] == s[i - 1] or p[j - 2] == ".")
                )
            elif p[j - 1] == "." or p[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1]
    return dp[m][n]


@pytest.mark.parametrize(
    "s,p,ex", [("aa", "a", False), ("aa", "a*", True), ("ab", ".*", True)]
)
def test_opt(s, p, ex):
    assert solve_optimal(s, p) == ex
