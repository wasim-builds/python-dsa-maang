"""
Problem: Valid Palindrome II
Difficulty: Easy  Companies: Meta,Amazon,Google
Problem Statement: Return true if string can become palindrome by removing at most one character.
Complexity: Time O(N), Space O(1)
"""

import pytest


def is_pal(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def solve_brute(s):
    return solve_optimal(s)


def solve_optimal(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return is_pal(s, l + 1, r) or is_pal(s, l, r - 1)
        l += 1
        r -= 1
    return True


@pytest.mark.parametrize("s,ex", [("aba", True), ("abca", True), ("abc", False)])
def test_opt(s, ex):
    assert solve_optimal(s) == ex
