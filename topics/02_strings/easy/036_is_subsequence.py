"""
Problem: Is Subsequence
Difficulty: Easy
Topic: 02_strings  Companies: Google,Amazon,Microsoft,Uber
Problem Statement: Given strings s and t, return true if s is a subsequence of t.
Complexity: Time O(N), Space O(1)
"""

import pytest


def solve_brute(s, t):
    it = iter(t)
    return all(c in it for c in s)


def solve_optimal(s, t):
    i = 0
    for c in t:
        if i < len(s) and c == s[i]:
            i += 1
    return i == len(s)


@pytest.mark.parametrize(
    "s,t,ex", [("ace", "abcde", True), ("aec", "abcde", False), ("", "abc", True)]
)
def test_opt(s, t, ex):
    assert solve_optimal(s, t) == ex
