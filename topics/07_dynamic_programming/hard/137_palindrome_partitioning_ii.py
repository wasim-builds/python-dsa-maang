"""
Problem: Palindrome Partitioning II
Difficulty: Hard  Companies: Google,Amazon,Microsoft
Problem Statement: Return minimum cuts needed for a palindrome partitioning of s.
Complexity: Time O(N^2), Space O(N^2)
"""

import pytest


def solve_brute(s):
    return solve_optimal(s)


def solve_optimal(s):
    n = len(s)
    is_pal = [[False] * n for _ in range(n)]
    for i in range(n):
        for l in range(i + 1):
            if s[l] == s[i] and (i - l <= 2 or is_pal[l + 1][i - 1]):
                is_pal[l][i] = True
    dp = [float("inf")] * n
    for i in range(n):
        if is_pal[0][i]:
            dp[i] = 0
            continue
        for j in range(1, i + 1):
            if is_pal[j][i]:
                dp[i] = min(dp[i], dp[j - 1] + 1)
    return dp[n - 1]


@pytest.mark.parametrize("s,ex", [("aab", 1), ("a", 0), ("ab", 1)])
def test_opt(s, ex):
    assert solve_optimal(s) == ex
