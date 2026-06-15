"""
Problem: Basic Calculator II
Difficulty: Hard  Companies: Amazon,Microsoft,Bloomberg
Problem Statement: Implement calculator to evaluate string with +,-,*,/ and spaces.
Complexity: Time O(N), Space O(N)
"""

import pytest


def solve_brute(s):
    return solve_optimal(s)


def solve_optimal(s):
    stack = []
    num = 0
    sign = "+"
    for i, c in enumerate(s):
        if c.isdigit():
            num = num * 10 + int(c)
        if (not c.isdigit() and c != " ") or i == len(s) - 1:
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(stack.pop() * num)
            elif sign == "/":
                stack.append(int(stack.pop() / num))
            sign = c
            num = 0
    return sum(stack)


@pytest.mark.parametrize("s,ex", [("3+2*2", 7), (" 3/2 ", 1), (" 3+5 / 2 ", 5)])
def test_opt(s, ex):
    assert solve_optimal(s) == ex
