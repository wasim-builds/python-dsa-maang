"""
Problem: Longest Common Prefix
Difficulty: Easy
Topic: 02_strings  Companies: Amazon,Google,Microsoft
Problem Statement: Write a function to find the longest common prefix string amongst an array of strings.
Complexity: Time O(S) where S is sum of all chars, Space O(1)
"""

import pytest
from typing import List


def solve_brute(strs):
    if not strs:
        return ""
    pref = strs[0]
    for s in strs[1:]:
        while not s.startswith(pref):
            pref = pref[:-1]
    return pref


def solve_optimal(strs):
    if not strs:
        return ""
    for i, c in enumerate(strs[0]):
        for s in strs[1:]:
            if i == len(s) or s[i] != c:
                return strs[0][:i]
    return strs[0]


@pytest.mark.parametrize(
    "strs,ex", [(["flower", "flow", "flight"], "fl"), (["dog", "racecar", "car"], "")]
)
def test_opt(strs, ex):
    assert solve_optimal(strs) == ex
