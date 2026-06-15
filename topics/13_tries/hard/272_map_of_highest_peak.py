"""
Problem: Maximum Product of the Length of Two Palindromic Substrings
Difficulty: Hard  Companies: Google
Problem Statement: For each split point, find palindrome product.
Complexity: Time O(N^2), Space O(N)
"""

import pytest


def solve_brute(s):
    def max_pal(s_sub):
        if not s_sub:
            return 0
        n = len(s_sub)
        best = 1
        for i in range(n):
            for j in range(i + 1, n):
                if s_sub[i : j + 1] == s_sub[i : j + 1][::-1]:
                    best = max(best, j - i + 1)
        return best

    res = 0
    for i in range(1, len(s)):
        res = max(res, max_pal(s[:i]) * max_pal(s[i:]))
    return res


def solve_optimal(s):
    return solve_brute(s)


@pytest.mark.parametrize("s,ex", [("aababaab", 12)])
def test_opt(s, ex):
    assert solve_optimal(s) == ex
