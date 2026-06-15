"""
Problem: Reverse Vowels of a String
Difficulty: Easy
Topic: 02_strings  Companies: Google,Amazon
Problem Statement: Given string s, reverse only vowels and return it.
Complexity: Time O(N), Space O(N)
"""

import pytest


def solve_brute(s):
    vowels = "aeiouAEIOU"
    v = [c for c in s if c in vowels]
    i = 0
    res = list(s)
    for j in range(len(res)):
        if res[j] in vowels:
            res[j] = v[-(i + 1)]
            i += 1
    return "".join(res)


def solve_optimal(s):
    vowels = set("aeiouAEIOU")
    s = list(s)
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and s[l] not in vowels:
            l += 1
        while l < r and s[r] not in vowels:
            r -= 1
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return "".join(s)


@pytest.mark.parametrize("s,ex", [("hello", "holle"), ("leetcode", "leotcede")])
def test_opt(s, ex):
    assert solve_optimal(s) == ex
