"""
Problem: Letter Combinations of a Phone Number
Difficulty: Easy  Companies: Amazon,Google,Meta,Microsoft
Problem Statement: Return all possible letter combinations from phone digit mapping.
Complexity: Time O(4^N * N), Space O(N)
"""

import pytest
from typing import List


def solve_brute(digits):
    return solve_optimal(digits)


def solve_optimal(digits):
    if not digits:
        return []
    phone = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    res = []

    def bt(i, cur):
        if i == len(digits):
            res.append(cur)
            return
        for c in phone[digits[i]]:
            bt(i + 1, cur + c)

    bt(0, "")
    return res


@pytest.mark.parametrize(
    "d,ex",
    [
        ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),
        ("2", ["a", "b", "c"]),
        ("", []),
    ],
)
def test_opt(d, ex):
    assert sorted(solve_optimal(d)) == sorted(ex)
