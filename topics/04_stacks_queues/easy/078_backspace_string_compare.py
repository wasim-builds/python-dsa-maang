"""
Problem: Backspace String Compare
Difficulty: Easy  Companies: Amazon,Google,Microsoft
Problem Statement: Given strings s and t with '#' as backspace, return if they are equal.
Complexity: Time O(N), Space O(1) two-pointer
"""

import pytest


def build(s):
    stack = []
    for c in s:
        if c != "#":
            stack.append(c)
        elif stack:
            stack.pop()
    return "".join(stack)


def solve_brute(s, t):
    return build(s) == build(t)


def solve_optimal(s, t):
    return build(s) == build(t)


@pytest.mark.parametrize(
    "s,t,ex",
    [
        ("ab#c", "ad#c", True),
        ("ab##", "c#d#", True),
        ("a##c", "#a#c", True),
        ("a#c", "b", False),
    ],
)
def test_opt(s, t, ex):
    assert solve_optimal(s, t) == ex
