"""
Problem: Basic Calculator
Difficulty: Hard  Companies: Google,Amazon,Microsoft
Problem Statement: Implement basic calculator to evaluate string with +, -, (, ).
Complexity: Time O(N), Space O(N)
"""

import pytest


def solve_brute(s):
    return solve_optimal(s)


def solve_optimal(s):
    stack = []
    num = 0
    sign = 1
    res = 0
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c in "+-":
            res += sign * num
            num = 0
            sign = 1 if c == "+" else -1
        elif c == "(":
            stack.append(res)
            stack.append(sign)
            res = 0
            sign = 1
        elif c == ")":
            res += sign * num
            num = 0
            res *= stack.pop()
            res += stack.pop()
    return res + sign * num


@pytest.mark.parametrize(
    "s,ex", [("1 + 1", 2), (" 2-1 + 2", 3), ("(1+(4+5+2)-3)+(6+8)", 23)]
)
def test_opt(s, ex):
    assert solve_optimal(s) == ex
