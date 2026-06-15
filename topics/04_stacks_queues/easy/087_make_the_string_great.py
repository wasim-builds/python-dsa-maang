"""
Problem: Make The String Great
Difficulty: Easy  Companies: Amazon,Google
Problem Statement: Remove pairs of same letter different case until none remain.
Complexity: Time O(N), Space O(N)
"""

import pytest


def solve_brute(s):
    return solve_optimal(s)


def solve_optimal(s):
    stack = []
    for c in s:
        if stack and stack[-1] != c and stack[-1].lower() == c.lower():
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)


@pytest.mark.parametrize(
    "s,ex", [("leEeetcode", "leetcode"), ("abBAcC", ""), ("s", "s")]
)
def test_opt(s, ex):
    assert solve_optimal(s) == ex
