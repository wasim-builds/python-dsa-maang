"""
Problem: String to Integer (atoi)
Difficulty: Medium
Topic: 02_strings  Companies: Amazon,Microsoft,Bloomberg
Problem Statement: Implement atoi to convert string to integer following the rules (whitespace, sign, digits, clamp).
Complexity: Time O(N), Space O(1)
"""

import pytest


def solve_brute(s):
    return solve_optimal(s)


def solve_optimal(s):
    s = s.lstrip()
    sign = 1
    res = 0
    INT_MAX, INT_MIN = 2**31 - 1, -(2**31)
    if not s:
        return 0
    if s[0] in "+-":
        sign = 1 if s[0] == "+" else -1
        s = s[1:]
    for c in s:
        if not c.isdigit():
            break
        res = res * 10 + int(c)
        if sign * res > INT_MAX:
            return INT_MAX
        if sign * res < INT_MIN:
            return INT_MIN
    return sign * res


@pytest.mark.parametrize(
    "s,ex",
    [("42", 42), ("   -42", -42), ("4193 with words", 4193), ("words and 987", 0)],
)
def test_opt(s, ex):
    assert solve_optimal(s) == ex
