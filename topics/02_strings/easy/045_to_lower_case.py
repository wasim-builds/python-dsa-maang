"""
Problem: To Lower Case
Difficulty: Easy
Topic: 02_strings  Companies: Amazon,Google
Problem Statement: Given string s, return lowercase version.
Complexity: Time O(N), Space O(N)
"""

import pytest


def solve_brute(s):
    return s.lower()


def solve_optimal(s):
    return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in s)


@pytest.mark.parametrize(
    "s,ex", [("Hello", "hello"), ("here", "here"), ("LOVELY", "lovely")]
)
def test_opt(s, ex):
    assert solve_optimal(s) == ex
