"""
Problem: First Unique Character in a String
Difficulty: Easy
Topic: 02_strings  Companies: Amazon,Bloomberg,Microsoft,Google
Problem Statement: Given string s, find first non-repeating character and return its index. Return -1 if none.
Complexity: Time O(N), Space O(1) since at most 26 keys
"""

import pytest
from collections import Counter


def solve_brute(s):
    for i, c in enumerate(s):
        if s.count(c) == 1:
            return i
    return -1


def solve_optimal(s):
    count = Counter(s)
    for i, c in enumerate(s):
        if count[c] == 1:
            return i
    return -1


@pytest.mark.parametrize("s,ex", [("leetcode", 0), ("loveleetcode", 2), ("aabb", -1)])
def test_opt(s, ex):
    assert solve_optimal(s) == ex
