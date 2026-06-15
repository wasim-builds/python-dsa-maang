"""
Problem: Minimum Window Substring
Difficulty: Hard
Topic: 02_strings  Companies: Amazon,Google,Meta,Microsoft,Bloomberg
Problem Statement: Given strings s and t, return minimum window substring of s containing all chars in t. Return "" if none.
Complexity: Time O(N), Space O(|t|) sliding window with counter
"""

import pytest
from collections import Counter


def solve_brute(s, t):
    res = ""
    need = Counter(t)
    for i in range(len(s)):
        for j in range(i + len(t), len(s) + 1):
            w = s[i:j]
            if all(Counter(w)[c] >= n for c, n in need.items()):
                if not res or len(w) < len(res):
                    res = w
    return res


def solve_optimal(s, t):
    if not t:
        return ""
    need = Counter(t)
    window = {}
    have = required = len(need)
    res = ""
    l = 0
    for r, c in enumerate(s):
        window[c] = window.get(c, 0) + 1
        if c in need and window[c] == need[c]:
            have -= 1
        while have == 0:
            if not res or r - l + 1 < len(res):
                res = s[l : r + 1]
            window[s[l]] -= 1
            if s[l] in need and window[s[l]] < need[s[l]]:
                have += 1
            l += 1
    return res


@pytest.mark.parametrize(
    "s,t,ex", [("ADOBECODEBANC", "ABC", "BANC"), ("a", "a", "a"), ("a", "aa", "")]
)
def test_opt(s, t, ex):
    assert solve_optimal(s, t) == ex


@pytest.mark.parametrize("s,t,ex", [("ADOBECODEBANC", "ABC", "BANC")])
def test_brute(s, t, ex):
    assert solve_brute(s, t) == ex
