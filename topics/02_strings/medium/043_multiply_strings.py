"""
Problem: Multiply Strings
Difficulty: Medium
Topic: 02_strings  Companies: Facebook,Amazon,Microsoft
Problem Statement: Given two non-negative integers num1 and num2 as strings, return the product as a string. No BigInteger.
Complexity: Time O(M*N), Space O(M+N)
"""

import pytest


def solve_brute(num1, num2):
    return str(int(num1) * int(num2))


def solve_optimal(num1, num2):
    if num1 == "0" or num2 == "0":
        return "0"
    m, n = len(num1), len(num2)
    pos = [0] * (m + n)
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            mul = int(num1[i]) * int(num2[j])
            p1, p2 = i + j, i + j + 1
            s = mul + pos[p2]
            pos[p2] = s % 10
            pos[p1] += s // 10
    res = "".join(map(str, pos)).lstrip("0")
    return res or "0"


@pytest.mark.parametrize("n1,n2,ex", [("2", "3", "6"), ("123", "456", "56088")])
def test_opt(n1, n2, ex):
    assert solve_optimal(n1, n2) == ex
