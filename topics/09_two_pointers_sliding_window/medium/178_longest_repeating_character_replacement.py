"""
Problem: Longest Repeating Character Replacement
Difficulty: Medium  Companies: Google,Amazon,Meta
Problem Statement: Replace at most k characters to make longest repeating-letter substring.
Complexity: Time O(N), Space O(1)
"""

import pytest


def solve_brute(s, k):
    res = 0
    for i in range(len(s)):
        count = {}
        max_f = 0
        for j in range(i, len(s)):
            count[s[j]] = count.get(s[j], 0) + 1
            max_f = max(max_f, count[s[j]])
            if (j - i + 1) - max_f <= k:
                res = max(res, j - i + 1)
    return res


def solve_optimal(s, k):
    count = {}
    l = max_f = res = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r], 0) + 1
        max_f = max(max_f, count[s[r]])
        if (r - l + 1) - max_f > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res


@pytest.mark.parametrize("s,k,ex", [("ABAB", 2, 4), ("AABABBA", 1, 4)])
def test_opt(s, k, ex):
    assert solve_optimal(s, k) == ex
